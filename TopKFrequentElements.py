class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        have a hastable to keep track of the frequency of numbers
        afterwards have an array that is sorted by the number of times a number shows up
        and then return a spliced version of the array up to the point K
        """
        check = {}
        for i in nums:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        freq = sorted(check, key=lambda x:check[x], reverse=True)
        
        return freq[:k]
        