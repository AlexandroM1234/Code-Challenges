"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""
def square_digits(num):
    newNum = str(num)
    total = ""
    
    for n in newNum:
        power = int(n) **2
        total += str(power)
    return int(total)


def tests():
    assert square_digits(9119), 811181
if __name__ == "__main__":
    tests()
    print("Everything passed")
