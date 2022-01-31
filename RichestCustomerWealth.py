"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has jth in bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

"""


class Solution:
    # def maximumWealth(self, accounts) -> int:
    #     """
    #     U
    #     given a list of lists for each item in the inner list add up the sum and return the largest total of the inner lists

    #     P
    #     loop throught the outer most list
    #     for each element in the inner list add them all up
    #     and return the largest total of the inner list items

    #     """
    #     total = 0
    #     for bank in accounts:
    #         bankSum = 0
    #         for i in bank:
    #             bankSum += i
    #         if bankSum > total:
    #             total = bankSum
    #     return total

    # another simpler implemention of this problem I did again for a daily leetcode question
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Have an output variable to keep track of the largest possible sum of money in each account
        output = 0
        # loop through the list
        for i in accounts:
            # for each list calculate the max sum comapring the previous max being the output and the sum of all the elements in the inner list
            output = max(output, sum(i))

        return output
