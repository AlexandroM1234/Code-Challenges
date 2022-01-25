"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # have a count for every jewel in a dictionary and have the value set to 0
        count = {}
        for char in jewels:
            count[char] = 0

        # loop through the stones and its in the count increment the value
        for j in stones:
            if j in count:
                count[j] += 1
        # then return the sum of all the values in the dictionary
        return sum(count.values())
