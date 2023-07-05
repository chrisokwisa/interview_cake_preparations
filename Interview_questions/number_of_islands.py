# Given a 2 dimensional grid of 1s (land blocks) and 0s (water blocks), count the number of 
# islands present in the grid. The definition of an island is as follows:
# 
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1s) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.

# Example:
# Input:
# 10001
# 11000
# 10110
# 00000

# Output: 3

class solution:
    def inRange(self, grid, r, c): # r = row, c = column 
        numRow, numCol = len(grid), len(grid[0]) # len(grid) = number of rows, len(grid[0]) = number of columns 
        if r < 0 or c < 0 or r >= numRow or c >= numCol: #
            return False 
        return True
    
    def numIslands(self, grid):
        numRow, numCol = len(grid), len(grid[0]) # len(grid) = number of rows, len(grid[0]) = number of columns. 
        # len(grid[0]) is the length of the first row in the grid
        visited = set()
        numIslands = 0
        for r in range(numRow):
            for c in range(numCol):
                if grid[r][c] == 1 and (r, c) not in visited: # if the current node is a 1 and the current node is not in visited
                    numIslands += 1 # increment the number of islands by 1
                    stack = [(r, c)]
                    while stack:
                        row, col = stack.pop()
                        visited.add((row, col))
                        for (nr, nc) in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]: # nr = new row, nc = new column 
                            if self.inRange(grid, nr, nc) and grid[nr][nc] == 1 and (nr, nc) not in visited: # if the new row and new column are in range and
                                #  the new row and new column are 1 and the new row and new column are not in visited
                                stack.append((nr, nc)) # append the new row and new column to the stack
        return numIslands



        # we can use a depth first search to solve this problem
        # we can use a stack to keep track of the nodes that we have visited
        # we can use a set to keep track of the nodes that we have visited
        # we can use a variable to keep track of the number of islands that we have visited
        # we can use a for loop to iterate through the rows of the grid
        # we can use a for loop to iterate through the columns of the grid
        # we can use a conditional statement to check if the current node is a 1
        # we can use a conditional statement to check if the current node is in the set of visited nodes
        # we can use a conditional statement to check if the current node is in range

        # solution 1

        # O(n) time complexity where n is the number of nodes in the  grid because we are iterating through the grid once. where 
        # O(n) space complexity where n is the number of nodes in the grid


    
        

grid = [[1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0]]

print(solution().numIslands(grid))
