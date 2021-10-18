"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for both strings itterate through them and check the counts of each letter and at the end compare if the hashmaps are the same if so return True otherwise False
        # another implementation is to have 1 hashmap and itterate through string one and decrement for string2 and then check if any of the values in the hashmap arent 0
        check1 = {}
        check2 = {}

        for i in s:
            if i in check1:
                check1[i] += 1
            else:
                check1[i] = 1

        for j in t:
            if j in check2:
                check2[j] += 1
            else:
                check2[j] = 1

        return check1 == check2
