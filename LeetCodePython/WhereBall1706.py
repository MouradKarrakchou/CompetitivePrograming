class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        L = [-2 for _ in range(len(grid[0]))]
        for k in range(len(grid[0])):
            currentRow = 0
            currentCollumn = k
            while (currentRow < len(grid)):
                direction = Solution.findBallextra(self, grid, currentCollumn, currentRow)
                if direction == 0:
                    L[k] = -1
                    break
                elif direction == 1:
                    currentCollumn += 1
                else:
                    currentCollumn -= 1
                currentRow+=1
            if L[k] != -1:
                L[k] = currentCollumn
        return(L)

    def findBallextra(self, grid, x, y):
        if x!=len(grid[0])-1 and grid[y][x] == 1 and grid[y][x + 1] == 1:
            return 1
        elif x!=0 and grid[y][x] == -1 and grid[y][x - 1] == -1:
            return -1
        else:
            return 0


print(Solution.findBall(Solution, [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
