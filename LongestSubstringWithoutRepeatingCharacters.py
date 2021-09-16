"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding door approach
        have a left and right pointer on the starting index
        have a set to keep track off all the unique characters
        when we find a character not in the set add it to the set and continue the right pointer forward
        and also keep track of the length of the set and the current max
        if we find a character in the set remove it and move the left pointer forward
        the loop ends when we hit the length of the string
        """
        l = 0
        r = 0
        output = 0

        check = set()

        while r < len(s):
            if s[r] not in check:
                check.add(s[r])
                r += 1
                output = max(len(check), output)
            else:
                check.remove(s[l])
                l += 1
        return output
