"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
 
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""


class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        # Have a global list to append the cur lists that contains the numbers that sum up to the target
        output = []

        # have a recursive helper function that does a dfs traversal
        # we need to keep track of the index we are on, the cur list of numbers that should add up to the target and the total so far
        def dfs(i, cur: List[int], total):
            # Base cases
            # if the total equals the target
            if total == target:
                # we append it to the output but make a copy so we keep the cur array the same if we need to keep traversing
                output.append(cur.copy())
                # then return so we break out of the function
                return
            # if the index is greater than the length of the given array or the running total is greater than the target we break out and return nothing
            if i >= len(c) or total > target:
                return
            # Other cases
            # Now that we continue one we append the value at the index to the current array
            cur.append(c[i])
            # we call the function again and pass in everything the same way except we increment the total
            dfs(i, cur, total + c[i])
            # after that traversal we pop off the last number in the current list
            cur.pop()
            # then instead of the same index we traverse to the next number and keep the total and current the same
            dfs(i + 1, cur, total)

        # Finally call the function passing in the starting index 0, our current is going to be an empty list to start and then the running total is going to be 0 to start
        dfs(0, [], 0)
        # finally after all the recursive call return the output list
        return output
