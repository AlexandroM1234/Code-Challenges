"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not). 

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 2 pointer solution to start with the beginnings of the strings
        i = 0
        j = 0

        # if there is no s it can technically be apart of t so return True
        if not len(s):
            return True

        # then while both indices are in range
        while i < len(s) and j < len(t):
            # if there is a point where the values match we found a letter in s so increment i to find the next
            if s[i] == t[j]:
                i += 1
            # in all cases we need to increment j
            j += 1
        # then at the end if i is equal to s then s is a subsequence of t otherwise return t
        return i == len(s)
