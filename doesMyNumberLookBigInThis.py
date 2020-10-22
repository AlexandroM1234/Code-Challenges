"""
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
"""

def narcissistic( value ):
    stringValue = str(value)
    power = len(stringValue)
    total = 0
    for num in stringValue:
        total += int(num) ** power
    if total == value:
        return True
    return False
        
def tests():
    assert narcissistic(7) == True, '7 is narcissistic'
    assert narcissistic(371) == True, '371 is narcissistic'
    assert narcissistic(122) == False, '122 is not narcissistic'
    assert narcissistic(4887) == False, '4887 is not narcissistic'
if __name__ == "__main__":
    tests()
    print("Everything passed")