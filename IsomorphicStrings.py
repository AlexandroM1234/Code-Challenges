"""
for every char in each string
have a hashtable where the key is the char and the value is the one of the opposite string
if they're not equal return false 
otherwise return true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tMap = {}
        sMap = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]

            if sChar not in sMap:
                sMap[sChar] = tChar
            if tChar not in tMap:
                tMap[tChar] = sChar
            if tMap[tChar] != sChar or sMap[sChar] != tChar:
                return False
        return True
