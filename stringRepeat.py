"""
Write a function called repeat_str which repeats the given string src exactly count times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
"""

def repeat_str(repeat, string):
    word = ""
    for _ in range(repeat):
        word += string
    return word

def tests():
    assert repeat_str(4, 'a') == 'aaaa'
    assert repeat_str(3, 'hello ') == 'hello hello hello '
    assert repeat_str(2, 'abc') == 'abcabc'



if __name__ == "__main__":
    tests()
    print("Everything passed")