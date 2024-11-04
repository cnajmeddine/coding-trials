class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create sets to track incoming and outgoing connections
        roads = set((a, b) for a, b in connections)
        graph = {i: [] for i in range(n)}
        
        # Build an undirected graph for traversing neighbors
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        changes = 0
        visited = set()
        
        # Depth-first traversal from city 0
        def dfs(city):
            nonlocal changes
            visited.add(city)
            for neighbor in graph[city]:
                if neighbor not in visited:
                    # Check if edge needs reorientation
                    if (neighbor, city) not in roads:
                        changes += 1
                    dfs(neighbor)
        
        dfs(0)
        return changes
