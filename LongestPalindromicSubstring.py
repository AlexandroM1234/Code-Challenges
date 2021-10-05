class Solution:
    """
    so define a helper method that takes in a left and right pointer that starts at the center of a point of the string i and builds the palindrome outwards
    after we keep building the palindrome outward until we hit the bounds of the string or the values at the left and right pointer dont match
    we then return the string that has the longest palidrome
    """

    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            # takes in a point in the string and starts building outward constantly checking if its a palindrome and stops when its not and returns the string
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1 : r]

        res = ""

        for i in range(len(s)):
            # for every index in the string we check if we can build a palindrome outwards from that point and we check and replace whenever we find a longer palindrome
            test = helper(i, i)

            if len(test) > len(res):
                res = test
            # we run the helper function again incase the string given is of even length
            test = helper(i, i + 1)
            if len(test) > len(res):
                res = test

        return res
