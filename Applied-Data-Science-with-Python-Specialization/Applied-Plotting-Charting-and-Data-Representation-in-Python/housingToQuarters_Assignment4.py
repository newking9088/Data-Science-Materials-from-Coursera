def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    import pandas as pd
    df= pd.read_csv("City_Zhvi_AllHomes.csv")
    #print(df.columns[1:7])
    df.rename(columns ={"State": "states"}, inplace= True)
    df= df.set_index(["states","RegionName"])
    df = df.iloc[:,49:250]
    
    def quarters(col):
        if col.endswith(("01", "02", "03")):
            s = col[:4] + "q1"
        elif col.endswith(("04", "05", "06")):
            s = col[:4] + "q2"
        elif col.endswith(("07", "08", "09")):
            s = col[:4] + "q3"
        else:
            s = col[:4] + "q4"
        return s  
    housing = df.groupby(quarters, axis = 1).mean()
    housing = housing.sort_index()
    return housing

convert_housing_data_to_quarters()

