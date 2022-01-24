"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        valid = 0

        for i in range(len(word)):
            if word[i].isupper():
                valid += 1

        return valid == len(word) or valid == 0 or valid == 1 and word[0].isupper()
