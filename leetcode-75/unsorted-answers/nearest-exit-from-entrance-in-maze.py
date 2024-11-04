from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Dimensions of the maze
        m, n = len(maze), len(maze[0])
        # Start BFS queue with entrance position and initial step count of 0
        queue = deque([(entrance[0], entrance[1], 0)])
        # Mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+'
        
        # Possible movement directions (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Process BFS
        while queue:
            x, y, steps = queue.popleft()
            
            # Explore all four possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if within bounds and is an empty cell
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    # Check if it's an exit (on the border and not the entrance)
                    if nx == 0 or ny == 0 or nx == m - 1 or ny == n - 1:
                        return steps + 1
                    
                    # Mark as visited and add to queue
                    maze[nx][ny] = '+'
                    queue.append((nx, ny, steps + 1))
        
        # No exit found
        return -1
