"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n, result = len(s), 0
        while n > 0:
            # start from the end of the word
            n -= 1
            # continue to add to the count if the character isn't a space
            if s[n] != " ":
                result += 1
            # now the edge case is assuming the last letter was a space and it continues because the result is still 0
            elif result > 0:
                return result
        return result