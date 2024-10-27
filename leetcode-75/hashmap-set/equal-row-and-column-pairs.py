class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        
        n = len(grid)
        row_counter = Counter(tuple(row) for row in grid)
        col_counter = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
        
        return sum(row_counter[row] * col_counter[row] for row in row_counter)
