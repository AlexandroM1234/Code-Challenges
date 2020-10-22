"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

# FIRST PASS SOLUTION
# def anagrams(word, words):
    # anagrams = []
    # count = {}
    # for char in word:
    #     if char not in count:
    #         count[char] = 1
    #     else:
    #         count[char] += 1
    # for word in words:
    #     check = {}
    #     for let in word:
    #         if let not in check:
    #             check[let] = 1
    #         else:
    #             check[let] += 1
    #     if check != count:
    #         continue
    #     else:
    #         anagrams.append(word)
    # return anagrams


# REFACTOR
def anagrams(word, words):
    return [w for w in words if sorted(word) == sorted(w)]

def tests():
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']

if __name__ == "__main__":
    tests()
    print("Everything passed")