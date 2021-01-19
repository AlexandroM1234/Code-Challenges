"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        # have an output variable and a count for the current tally of zeros in the list
        output = 0
        count = 0
        # loop through the list and add to the count if the number is equal to 1
        for num in nums:
            if num == 1:
                count += 1
            else:
                # Once there is a 0 in the list the number of consecutive 1s stops
                # then if the current count is greater than the current ouput replace the value of the current output to the current count
                if count > output:
                    output = count
                # then the count resets to 0 then continues to itterate through the list
                count = 0
        # The edge case is if there is only one item in the list and the count will only be applied once
        # if the single number is a one the count will be greater than the output and then you return the count
        if count > output:
            return count
        # if the single number is a zero the count will contine to be 0 and so will the output so return the output
        return output