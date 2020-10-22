"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
def solution(s):
    pairs = []
    if len(s) == 0 :
        return []
    if len(s) == 1:
        return [s+"_"]
    for i in range(0,len(s),2):
        pairs.append(s[i:i+2])
    for strings in pairs:
        if len(strings) == 1:
            pairs.remove(strings)
            pairs.append(strings+"_")
            return pairs
    return pairs

def tests():
    assert solution("asdfadsf"), ['as', 'df', 'ad', 'sf']
    assert solution("asdfads"), ['as', 'df', 'ad', 's_']
    assert solution("x"), ['x_']

if __name__ == "__main__":
    tests()
    print("Everything passed")
