#Load the energy data from the file Energy Indicators.xls, which is a list of
#indicators of energy supply and renewable electricity production from the
#United Nations for the year 2013, and should be put into a DataFrame with
#the variable name of energy. Keep in mind that this is an Excel file, and
#not a comma separated values file. Also, make sure to exclude the footer
#and header information from the datafile. The first two columns are
#unneccessary, so you should get rid of them.

def answer_one():
    import pandas as pd
    import numpy as np
    # skip first 17 rows, skip last 38 rows, usecols from C to F, A and B cols are empty
    energy = pd.read_excel('Energy Indicators.xls', skipfooter=38, skiprows=17, usecols = "C:F")
    col_names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = col_names
    energy.loc[energy['Energy Supply'] == '...'] = np.NaN
    # make sure the 'Energy Supply', and 'Energy Supply per Capita' are numetric not string
    energy[['Energy Supply', 'Energy Supply per Capita']] = energy[['Energy Supply', 'Energy Supply per Capita']].apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*10**6
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    energy['Country'] = energy['Country'].str.replace(r"([0-9]+)$","")
    replace_dict={"Republic of Korea": "South Korea",
                  "United States of America": "United States",
                  "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                  "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy['Country'].replace(to_replace=replace_dict, inplace=True)
    energy.reset_index()
    energy = energy.set_index('Country')
    #return energy
#print(answer_one())

#Next, load the GDP data from the file world_bank.csv, which is a csv containing
#countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

#Make sure to skip the header, and rename the following list of countries:

#"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran",
#"Hong Kong SAR, China": "Hong Kong"
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    replace_dict = {"Korea, Rep.": "South Korea", 
                    "Iran, Islamic Rep.": "Iran",
                    "Hong Kong SAR, China": "Hong Kong"
                   }
    GDP['Country Name'].replace(to_replace=replace_dict, inplace=True)
    years_to_keep = np.arange(2006, 2016).astype(str)
    GDP = GDP[np.append(['Country Name'],years_to_keep)]
    GDP.reset_index()
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    GDP = GDP.set_index('Country')

#Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering
#and Power Technology from the file scimagojr-3.xlsx, which ranks countries
#based on their journal contributions in the aforementioned area. Call this
#DataFrame ScimEn.
    ScimEn = pd.read_excel('scimagojr-3.xlsx', header=0)
    ScimEn.reset_index()
    ScimEn = ScimEn.set_index('Country')
#Join the three datasets: GDP, Energy, and ScimEn into a
#new dataset (using the intersection of country names). Use only the last
#10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr
#'Rank' (Rank 1 through 15). The index of this DataFrame should be the name
#of the country, and the columns should be ['Rank', 'Documents',
#'Citable documents', 'Citations', 'Self-citations', 'Citations per document'
#, 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable',
#'2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    first_merge = pd.merge(energy, GDP, how='outer', left_index=True, right_index=True)
    result = pd.merge(ScimEn, first_merge, how='outer', left_index=True, right_index=True)
    result = result.reset_index().dropna(thresh=result.shape[1]-10).set_index('Country')
    result = result.loc[result['Rank']<=15]
    return result

answer_one()

#The previous question joined three datasets then reduced this to just the top
#15 entries. When you joined the datasets, but before you reduced this to the
#top 15 items, how many entries did you lose?
def answer_two():
    import pandas as pd
    import numpy as np
    energy = pd.read_excel('Energy Indicators.xls', skipfooter=38, skiprows=17, usecols='C:F')
    col_names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = col_names
    energy.loc[energy['Energy Supply'] == '...'] = np.NaN
    energy[['Energy Supply', 'Energy Supply per Capita']] = energy[['Energy Supply', 'Energy Supply per Capita']].apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*10**6
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    energy['Country'] = energy['Country'].str.replace(r"([0-9]+)$","")
    replace_dict={"Republic of Korea": "South Korea",
                  "United States of America": "United States",
                  "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                  "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy['Country'].replace(to_replace=replace_dict, inplace=True)
    energy.reset_index()
    energy = energy.set_index('Country')
    en_shape = energy.shape
    
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    replace_dict = {"Korea, Rep.": "South Korea", 
                    "Iran, Islamic Rep.": "Iran",
                    "Hong Kong SAR, China": "Hong Kong"
                   }
    GDP['Country Name'].replace(to_replace=replace_dict, inplace=True)
    years_to_keep = np.arange(2006, 2016).astype(str)
    GDP = GDP[np.append(['Country Name'],years_to_keep)]
    GDP.reset_index()
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    GDP = GDP.set_index('Country')
    GDP_shape = GDP.shape
    
    ScimEn = pd.read_excel('scimagojr-3.xlsx', header=0)
    ScimEn.reset_index()
    ScimEn = ScimEn.set_index('Country')
    ScimEn_shape = ScimEn.shape
    
    first_merge = pd.merge(energy, GDP, how='outer', left_index=True, right_index=True)
    result = pd.merge(ScimEn, first_merge, how='outer', left_index=True, right_index=True)
    #result = result.reset_index().dropna(thresh=result.shape[1]-10).set_index('Country')
    result = result.shape[0]-15
    
    return result

answer_two()

#What is the average GDP over the last 10 years for each country?
#(exclude missing values from this calculation.)This function should return a
#Series named avgGDP with 15 countries and their average GDP sorted in
#descending order.
def answer_three():
    import numpy as np
    Top15 = answer_one()
    years_to_keep = np.arange(2006, 2016).astype(str)
    Top15['avgGDP'] = Top15[years_to_keep].mean(axis=1)
    return Top15['avgGDP'].sort_values(ascending=False)

answer_three()

#By how much had the GDP changed over the 10 year span for the country with
#the 6th largest average GDP?
def answer_four():
    import numpy as np
    Top15 = answer_one()
    years_to_keep = np.arange(2006, 2016).astype(str)
    Top15['avgGDP'] = Top15[years_to_keep].mean(axis=1)
    Top15 = Top15.sort_values(['avgGDP'], ascending=False)
    Top15['deltaGDP'] = Top15['2015'] - Top15['2006']
    Top15 = Top15.reset_index()
    return Top15.loc[5, 'deltaGDP']
answer_four()

#What is the mean Energy Supply per Capita?
def answer_five():
    import numpy as np
    Top15 = answer_one()
    result = Top15['Energy Supply per Capita'].mean(axis=0)
    return result

answer_five()

#What country has the maximum % Renewable and what is the percentage?
def answer_six():
    import numpy as np
    Top15 = answer_one()
    result = Top15['% Renewable'].idxmax()
    return (result, Top15.loc[result, '% Renewable'])

answer_six()

#Create a new column that is the ratio of Self-Citations to Total Citations.
#What is the maximum value for this new column, and what country has the highest ratio?
def answer_seven():
    import numpy as np
    Top15 = answer_one()
    Top15['CitationRatio'] = Top15['Self-citations']/Top15['Citations']
    result = Top15['CitationRatio'].idxmax()
    return (result, Top15.loc[result, 'CitationRatio'])

answer_seven()

#Create a column that estimates the population using Energy Supply and Energy
#Supply per capita. What is the third most populous country according to this estimate?
def answer_eight():
    import numpy as np
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15 = Top15.sort_values(['PopEst'], ascending=False)
    Top15 = Top15.reset_index()
    return Top15.loc[2, 'Country']

answer_eight()

#Create a column that estimates the number of citable documents per person.
#What is the correlation between the number of citable documents per capita
#and the energy supply per capita? Use the .corr() method, (Pearson's correlation).
def answer_nine():
    import numpy as np
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['Citable docs per Person'] = Top15['Citable documents']/Top15['PopEst']
    result = Top15.corr()
    return result.loc['Citable docs per Person', 'Energy Supply per Capita']

answer_nine()

# plot the data
def plot9():
    import matplotlib as plt
    #%matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])

#Create a new column with a 1 if the country's % Renewable value is at or above
#the median for all countries in the top 15, and a 0 if the country's % Renewable
#value is below the median.
def answer_ten():
    import numpy as np
    Top15 = answer_one()
    Top15['median % Renewable'] = Top15['% Renewable'].median()
    Top15['HighRenew'] = Top15['% Renewable'] >= Top15['median % Renewable']
    return Top15['HighRenew'].sort_values(ascending=True)

answer_ten()

#Use the following dictionary to group the Countries by Continent, then create
#a dateframe that displays the sample size (the number of countries in each continent bin),
#and the sum, mean, and std deviation for the estimated population of each country.
#ContinentDict  = {'China':'Asia', 
#                  'United States':'North America', 
#                  'Japan':'Asia', 
#                  'United Kingdom':'Europe', 
#                  'Russian Federation':'Europe', 
#                  'Canada':'North America', 
#                  'Germany':'Europe', 
#                  'India':'Asia',
#                  'France':'Europe', 
#                  'South Korea':'Asia', 
#                  'Italy':'Europe', 
#                  'Spain':'Europe', 
#                  'Iran':'Asia',
#                  'Australia':'Australia', 
#                  'Brazil':'South America'}

def answer_eleven():
    import numpy as np
    import pandas as pd
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia',
                      'United States':'North America', 
                      'Japan':'Asia',
                      'United Kingdom':'Europe',
                      'Russian Federation':'Europe',
                      'Canada':'North America',
                      'Germany':'Europe', 
                      'India':'Asia',
                      'France':'Europe', 
                      'South Korea':'Asia', 
                      'Italy':'Europe', 
                      'Spain':'Europe', 
                      'Iran':'Asia',
                      'Australia':'Australia', 
                      'Brazil':'South America'}
    Top15 = Top15.reset_index()
    Top15['Continent'] = Top15['Country'].map(ContinentDict)
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    result = Top15.copy()
    result = result[['Continent', 'PopEst']]
    result = result.groupby('Continent')['PopEst'].aggregate(['size','sum', 'mean','std'])
    #result = grouped.agg(['np.size', 'sum', 'mean', 'std'])
    idx = pd.IndexSlice
    #result = result.loc[:, idx['PopEst']]
    #result = result.reset_index()
    #result = result.set_index('Continent')
    return result

answer_eleven()

#Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new
#% Renewable bins. How many countries are in each of these groups?
def answer_twelve():
    import numpy as np
    import pandas as pd
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia',
                      'United States':'North America', 
                      'Japan':'Asia',
                      'United Kingdom':'Europe',
                      'Russian Federation':'Europe',
                      'Canada':'North America',
                      'Germany':'Europe', 
                      'India':'Asia',
                      'France':'Europe', 
                      'South Korea':'Asia', 
                      'Italy':'Europe', 
                      'Spain':'Europe', 
                      'Iran':'Asia',
                      'Australia':'Australia', 
                      'Brazil':'South America'}
    Top15 = Top15.reset_index()
    Top15['Continent'] = Top15['Country'].map(ContinentDict)
    Top15['% Renewable'] = pd.cut(Top15['% Renewable'], 5)
    result = Top15.groupby(['Continent', '% Renewable'])['Country'].count()
    result = result.reset_index()
    #result.drop('Country', axis=1, inplace=True)
    
    result = result.set_index(['Continent', '% Renewable'])
    return result['Country']

answer_twelve()

#Convert the Population Estimate series to a string with thousands separator
#(using commas). Do not round the results.
def answer_thirteen():
    import numpy as np
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['PopEst'] = Top15['PopEst'].apply('{:,}'.format)
    return Top15['PopEst']

answer_thirteen()

#visualization example
def plot_optional():
    import matplotlib.pyplot as plt
    #%matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
    plt.show()
    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")

plot_optional()
