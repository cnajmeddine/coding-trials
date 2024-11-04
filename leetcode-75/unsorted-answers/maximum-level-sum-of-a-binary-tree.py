class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf')
        max_level = 1
        level = 1
        queue = [root]
        
        while queue:
            level_sum = sum(node.val for node in queue)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            queue = next_level
            level += 1
        
        return max_level
