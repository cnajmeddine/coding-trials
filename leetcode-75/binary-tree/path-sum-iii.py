class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            path_count = prefix_sums.get(current_sum - targetSum, 0)
            
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            prefix_sums[current_sum] -= 1
            
            return path_count
        
        prefix_sums = {0: 1}
        return dfs(root, 0)
