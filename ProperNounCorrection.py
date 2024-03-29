"""
Proper nouns always begin with a capital letter, followed by small letters.

Correct a given proper noun so that it fits this statement.

Example

For noun = "pARiS", the output should be
properNounCorrection(noun) = "Paris";
For noun = "John", the output should be
properNounCorrection(noun) = "John".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string noun

A string representing a proper noun with a mix of capital and small English letters.

Guaranteed constraints:
1 ≤ noun.length ≤ 10.

[output] string

Corrected (if needed) noun
"""


def properNounCorrection(noun):
    # remember in python you can't replace strings in place so you have to have an output string for and loop through the given string
    output = ""
    output += noun[0].upper()
    for i in range(1, len(noun)):
        output += noun[i].lower()
    return output
