"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:

Input: matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
],
target = 3
Output: true
Example 2:


Input: matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
],
target = 13
Output: false
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Basically because the numbers on the left column are also sorted we can do binary search on the first column to find out what column the target is in and then binary search on the row we find
        rows, cols = len(matrix), len(matrix[0])
        
        top, bot = 0, rows - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l,r = 0, cols - 1
        
        while l <=  r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False