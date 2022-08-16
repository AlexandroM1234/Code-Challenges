import enum


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        loop through the string and add the letter to the hashtable and the key will be the             letter and the value will be the amount of times it shows up in the string
        once the hashtable is filled loop through the string and then if the value of it is 1 in
        the table return its idx otherwise return -1
        time complexity: O(n)
        space complexity: O(n)
        """
        check = {}
        for i in range(len(s)):
            if s[i] not in check:
                check[s[i]] = 1
            else:
                check[s[i]] += 1
        for i in range(len(s)):
            if check[s[i]] == 1:
                return i
        return -1

    def firstUniqCharV2(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
        for i, let in enumerate(s):
            if count[let] == 1:
                return i
        return -1
