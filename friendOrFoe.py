"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.
"""
def friend(x):
    return [friends for friends in x if len(friends) == 4]


    
def tests():
    assert friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"]
if __name__ == "__main__":
    tests()
    print("Everything passed")