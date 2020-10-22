"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
"""

def likes(names):
    if len(names) == 0 or None:
        return "no one likes this"
    
    for i in range(len(names)):
        if len(names) == 1:
            return F"{names[i]} likes this"
        elif len(names) == 2:
            return F"{names[i]} and {names[i+1]} like this"
        elif len(names) == 3:
            return F"{names[i]}, {names[i+1]} and {names[i+2]} like this"
        else:
            return F"{names[i]}, {names[i+1]} and {len(names)-2} others like this"

def tests():
    assert likes([]), 'no one likes this'
    assert likes(['Peter']), 'Peter likes this'
    assert likes(['Jacob', 'Alex']), 'Jacob and Alex like this'
    assert likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this'



if __name__ == "__main__":
    tests()
    print("Everything passed")