from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    flag = 0
                    # Check top
                    if i > 0 and grid[i-1][j] == 1:
                        flag += 1
                    # Check bottom
                    if i < row - 1 and grid[i+1][j] == 1:
                        flag += 1
                    # Check right
                    if j < col - 1 and grid[i][j+1] == 1:
                        flag += 1
                    # Check left
                    if j > 0 and grid[i][j-1] == 1:
                        flag += 1
                    
                    # Each land cell has 4 sides, reduce shared sides
                    if flag == 0:
                        count += 4
                    elif flag == 1:
                        count += 3
                    elif flag == 2:
                        count += 2
                    elif flag == 3:
                        count += 1
                    elif flag == 4:
                        count += 0

        return count
