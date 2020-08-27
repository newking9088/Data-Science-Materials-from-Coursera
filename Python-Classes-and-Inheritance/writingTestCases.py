"""Testing functions:
A function defines an operation that can be performed. If the function takes one
or more parameters, it is supposed to work properly on a variety of possible
inputs. Each test case will check whether the function works properly on one
set of possible inputs. A useful function will do some combination of three
things, given its input parameters:
A) Return a value. For these, you will write return value tests.
B) Modify the contents of some mutable object, like a list or dictionary.
 For these you will write side effect tests.
C) Print something or write something to a file. Tests of whether a function
 generates the right printed output are beyond the scope of this testing
 framework; you won’t write these tests.

 RETURN VALUE TEST"""
def square(x):
    return x*x

import test

test.testEqual(square(3), 9)

"""Side Effect Tests:
To test whether a function makes correct changes to a mutable object, you will
need more than one line of code. You will first set the mutable object to some
value, then run the function, then check whether the object has the expected
value. Call this a side effect test because you are checking to see whether
the function invocation has had the correct side effect on the mutable object."""
def update_counts(letters, counts_dict):
    for c in letters:
        counts_dict[c] = 1
        if c in counts_dict:
            counts_dict[c] = counts_dict[c] + 1

import test

counts_dict = {'a': 3, 'b': 2}
update_counts("aaab", counts_dict)
# 3 more occurrences of a, so 6 in all
test.testEqual(counts_dict['a'], 6)
# 1 more occurrence of b, so 3 in all
test.testEqual(counts_dict['b'], 3)

"""Testing Conditionals and Loops
f the code has a conditional execution, or a for loop, then you’ll want to
include test cases that exercise different possible paths through the code.
For example, if there is a for loop, edge cases would include iteration
through an empty sequence or a sequence with just one item. With a
conditional, you would want different inputs that cause the if and
else clauses to execute.

Testing Optional Parameters
If a function takes an optional parameter, one of the edge cases to test
for is when no parameter value is supplied during execution. Below are
some tests for the built-in sorted function."""
import test

test.testEqual(sorted([1, 7, 4]), [1, 4, 7])
test.testEqual(sorted([1, 7, 4], reverse=True), [7, 4, 1])

"""test-2-1: If you write a complete set of tests and a function passes
all the tests, you can be sure that it’s working correctly.
A. True
B. False     ( Correct )
The tests should cover as many edge cases as you can think of, but there's
always a possibility that the function does badly on some input that you
didn't include as a test case."""

