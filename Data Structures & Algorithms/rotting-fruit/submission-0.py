from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        grid_copy = deepcopy(grid)
        count  = 0 
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] == 2 :
                    queue.append((r,c)) 
                elif grid_copy[r][c] == 1:
                    count += 1 
        minute = 0 
        while len(queue) != 0 and count >0 :
            minute += 1 
            total_rotten = len(queue)
            for _ in range(total_rotten):
                x,y = queue.popleft()
                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    new_x, new_y = x+dx, y+dy
                    if new_x < 0 or new_y < 0 or new_x >= rows or new_y >= cols:
                        continue 
                    if grid_copy[new_x][new_y] == 0 or grid_copy[new_x][new_y]==2:
                        continue 
                    count -= 1 
                    grid_copy[new_x][new_y] = 2 
                    queue.append((new_x,new_y))
        
        if count >0 :
            return -1 
        return minute 


        
            