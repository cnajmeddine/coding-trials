from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            x, y, steps = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if nx == 0 or ny == 0 or nx == m - 1 or ny == n - 1:
                        return steps + 1
                    maze[nx][ny] = '+'
                    queue.append((nx, ny, steps + 1))
        return -1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0
        while queue:
            x, y, time = queue.popleft()
            minutes = max(minutes, time)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny, time + 1))
                    fresh -= 1
        
        return minutes if fresh == 0 else -1
