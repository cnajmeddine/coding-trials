class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Graph to store variables and their division values
        graph = defaultdict(dict)
        
        # Build the graph from the equations
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value
        
        # DFS to find division path
        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0
            if src == dest:
                return 1.0
            
            visited.add(src)
            for neighbor, val in graph[src].items():
                if neighbor not in visited:
                    res = dfs(neighbor, dest, visited)
                    if res != -1.0:
                        return res * val
            visited.remove(src)
            return -1.0
        
        # Process each query
        result = []
        for C, D in queries:
            result.append(dfs(C, D, set()))
        
        return result
