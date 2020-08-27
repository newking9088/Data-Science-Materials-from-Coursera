"""To write a unit test, we must know the correct result when calling the
function with a specific input."""
def square(x):
    '''raise x to the second power'''
    return x * x

import test   # works only in runstone..not Python
print('testing square function')
test.testEqual(square(10), 100)
test.testEqual(square(-4),16)
test.testEqual(square(1.5),2.25)   # checking all t possible cases
test.testEqual(square(0),16)

# First function is function to be tested...second value is expected correct value
"""test-1-1: When test.testEqual() is passed two values that are not the same,
it generates an error and stops execution of the program.
A. True
B. False    (Correct)
C. It depends
A message is printed out, but the program does not stop executing"""

"""test-1-2: Test cases are a waste of time, because the python interpreter will give
an error message when the program runs incorrectly, and that’s all you need for debugging.
A. True
B. False  (Correct)
Test cases let you test some pieces of code as you write them, rather than waiting for
problems to show themselves later."""

"""test-1-3: Which of the following is the correct way to write a test to check that ‘under’
will be blanked as 'u_d__' when the user has guessed letters d and u so far?"""

def blanked(word, revealed_letters):
    return word

import test

test.testEqual(blanked('hello', 'elj'), "_ell_")
test.testEqual(blanked('hello', ''), '_____')
test.testEqual(blanked('ground', 'rn'), '_r__n_')
test.testEqual(blanked('almost', 'vrnalmqpost'), 'almost')
"""A. test.testEqual(blanked('under', 'du', 'u_d__'))
B. test.testEqual(blanked('under', 'u_d__'), 'du')
C. test.testEqual(blanked('under', 'du'), 'u_d__')  (Correct)
This checks whether the value returned from the blanked function is 'u_d__'."""
