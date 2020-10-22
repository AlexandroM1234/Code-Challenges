"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""

def duplicate_encode(word):
    output = ""
    
    count = {}
    
    word = word.lower()
    
    for char in word:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    for let in word:
        if let in count and count[let]==1:
            output += "("
        if let in count and count[let] > 1:
            output += ")"
    return output

def tests():
    assert duplicate_encode("din"),"((("
    assert duplicate_encode("recede"),"()()()"
    assert duplicate_encode("Success")==")())())","should ignore case"
    assert duplicate_encode("(( @"),"))(("


if __name__ == "__main__":
    tests()
    print("Everything passed")