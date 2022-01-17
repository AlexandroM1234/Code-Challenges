"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Have a set to keep track of the numbers we've seen
        check = set()

        for i in arr:
            # calculate the numbers we have to look for in the set
            # Also dont do floor division we are looking for the strict half of the number or double
            if i * 2 in check or i / 2 in check:
                # return True if we find a number we are looking for that meets the critera
                return True
            check.add(i)
        # Return False if we make it through the loop without finding any numbers that work
        return False
