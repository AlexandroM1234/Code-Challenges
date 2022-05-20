from collections import defaultdict

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # setup a hashmap with the default values being a list
        res = defaultdict(list)
        
        # for each string in the list of strings
        for s in strs:
            # setup a count array representing each letter in the alphabet
            count = [0] * 26
            # for each character in the string
            for c in s:
                # get the ascii value of the character subtract it from the ascii value of a and that gives us our index for the count array
                # then each time a letter appears increment the value in the array by 1
                count[ord(c) - ord("a")] +=  1
                 
                # Ex. a -> 80 - 80 = 0 so a is the first index so on so fourth
                # then index 0 == "a" = 1 or count[0] = 1
            
            # then after the count is created for each string make the count array a tuple because arrays can't be keys then append the string to the array in the hashmap
            res[tuple(count)].append(s)

        # finally return the values in the hashmap
        return res.values()