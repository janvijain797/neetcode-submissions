from collections import deque 
class Solution:
        def bfs(self,r,c,visited,rows,cols,grid):
            queue = deque()
            queue.append((r,c))
            visited[r][c] = 1 
            area = 1 
            while len(queue) != 0:
                x,y = queue.popleft()
                for xx, yy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_i , new_j = x+xx , y+yy 
                    if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                        continue 
                    if grid[new_i][new_j] == 0:
                        continue 
                    if visited[new_i][new_j] == 1:
                        continue 
                    visited[new_i][new_j] = 1 
                    queue.append((new_i, new_j))
                    area += 1 
            return area 
        
        def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            rows = len(grid)
            cols = len(grid[0])
            visited = [[0 for _ in range(cols)] for _ in range(rows)]
            max_area = 0 
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and visited[r][c] == 0 :
                        area = self.bfs(r,c,visited,rows, cols,grid)
                        max_area  = max(max_area, area)
            return max_area
       