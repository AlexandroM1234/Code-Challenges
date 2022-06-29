"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If there is no grid return 0
        if not grid:
            return 0
        # setup your number of rows and columns
        rows, cols = len(grid), len(grid[0])

        # have a set to keep track of pairs you've visited
        visited = set()
        # keep track of the number of islands
        islands = 0

        # The BFS takes in the row and column
        def bfs(r, c):
            # have a queue incase you have a lot of neighbors to keep traversing
            q = []
            # add the row and column to the set to mark it visited
            visited.add((r, c))
            # add the current row and column to the queue
            q.append((r, c))

            # while something is in the queue
            while q:
                # pop the first row and column in the queue
                row, col = q.pop(0)
                # you directions of right left top bottom
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # loop through the directions
                for dr, dc in directions:
                    if (
                        # check if the row and column from the input is valid with the directions from the array
                        (row + dr) in range(rows)
                        and (col + dc) in range(cols)
                        # check if the position we are on is an island and that its not visited
                        and grid[dr + row][dc + col] == "1"
                        and (row + dr, col + dc) not in visited
                    ):
                        # Add that row and col to the queue
                        q.append((row + dr, col + dc))
                        # and add it to the visited set
                        visited.add((row + dr, col + dc))

        # Loop through the grid itself
        for r in range(rows):
            for c in range(cols):
                # if the position we are on is not in visited and its an island
                if grid[r][c] == "1" and (r, c) not in visited:
                    # call the bfs function and pass in the row and column
                    bfs(r, c)
                    # finally add to the number of islands
                    islands += 1

        # then return the total number of islands
        return islands
