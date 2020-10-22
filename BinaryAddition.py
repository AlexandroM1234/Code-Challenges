"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a,b):
    #your code here
    sum = a+b
    return bin(sum).replace("0b","")

def tests():
    assert add_binary(1,1),"10"
    assert add_binary(0,1),"1"
    assert add_binary(1,0),"1"
    assert add_binary(2,2),"100"
    assert add_binary(51,12),"111111"
if __name__ == "__main__":
    tests()
    print("Everything passed")