"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
Example 1:
Input: arr = [2,2,3,4]

Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]

Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Example 4:
Input: arr = [5]
Output: -1

Example 5:
Input: arr = [7,7,7,7,7,7,7]
Output: 7
"""


class Solution:
    def findLucky(self, arr: [int]) -> int:
        # setup a hastable where the keys are the numbers in the array and the value is the number of times they appear in the array
        count = {}
        # Have a largest variable for later use whose value may or may not change
        largest = 0
        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        # Once the hashtable is filled loop through it and find where the keys and the values are the same
        # After you find where the keys and values match compare it to the current largest and if its greater than the current largest change the value of largest
        for nums in count:
            if count[nums] == nums and nums > largest:
                largest = nums
        # In the case that none of the numbers appear the ammount of times of that number largest will remain 0 and then return a -1
        if largest == 0:
            return -1
        # after looping through the hashtable the largest is found and return it
        return largest
