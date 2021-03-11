"""
Determine whether the given string can be obtained by one concatenation of some string to itself.

Example

For inputString = "tandemtandem", the output should be
isTandemRepeat(inputString) = true;
For inputString = "qqq", the output should be
isTandemRepeat(inputString) = false;
For inputString = "2w2ww", the output should be
isTandemRepeat(inputString) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
2 ≤ inputString.length ≤ 20.

[output] boolean

true if inputString represents a string concatenated to itself, false otherwise.
"""


def isTandemRepeat(inputString):
    # if the first half of the string is equal to the second then you cab get the same string from one concatenation so return True
    half = len(inputString) // 2
    return inputString[:half] == inputString[half:]
