class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        row = len(grid)
        column = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1":
                    dfs(grid, row, column, i, j)
                    count += 1
        return count

def dfs(grid, row, column, x, y):
    if grid[x][y] == "0":
        return
    grid[x][y] = "0"

    if x != 0:
        dfs(grid, row, column, x-1, y)
    if x != row - 1:
        dfs(grid, row, column, x+1, y)
    if y != 0:
        dfs(grid, row, column, x, y-1)
    if y != column - 1:
        dfs(grid, row, column, x, y+1)
