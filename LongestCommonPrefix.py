"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # start the loop at the first string
        for i in range(len(strs[0])):
            # then for all of the strings in the list
            for s in strs:
                # if u reach the end or if the character at i isnt equal to a valid letter in the first word return the res
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # otherwise we find common letters and add them to the res
            res += strs[0][i]
        # then return the res
        return res
