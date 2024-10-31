class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, length):
            if not node:
                return length - 1
            
            self.longest = max(self.longest, length)
            
            if direction == "left":
                dfs(node.left, "right", length + 1)
                dfs(node.right, "left", 1)
            else:
                dfs(node.right, "left", length + 1)
                dfs(node.left, "right", 1)
        
        self.longest = 0
        dfs(root, "left", 0)
        dfs(root, "right", 0)
        return self.longest
