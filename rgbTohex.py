import unittest
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    def limit(x):
        return max(0, min(x, 255))

    return "{0:02X}{1:02X}{2:02X}".format(limit(r), limit(g), limit(b))

def tests():
    assert rgb(0,0,0) =="000000", "testing zero values"
    assert rgb(1,2,3) =="010203", "testing near zero values"
    assert rgb(255,255,255)== "FFFFFF", "testing max values"
    assert rgb(254,253,252) == "FEFDFC", "testing near max values"
    assert rgb(-20,275,125) == "00FF7D", "testing out of range values"

if __name__ == "__main__":
    tests()
    print("Everything passed")