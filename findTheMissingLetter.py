import string
"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

"""
def find_missing_letter(chars):
    charset = string.ascii_lowercase if chars[0] >= "a" else string.ascii_uppercase
    for letter in charset[charset.index(chars[0]):]:
        if letter not in chars:
            return letter[0]

def tests():
    assert find_missing_letter(['a','b','c','d','f']), 'e'
    assert find_missing_letter(['O','Q','R','S']), 'P'
if __name__ == "__main__":
    tests()
    print("Everything passed")