class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        zeros_count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            max_len = max(max_len, right - left)
        
        return max_len
