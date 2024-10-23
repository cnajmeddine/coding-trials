class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2
        
        # Binary search on the smaller array nums1
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2  # Midpoint for nums1
            j = half_len - i  # Corresponding point in nums2
            
            # Edge cases for binary search boundaries
            nums1_left_max = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right_min = nums1[i] if i < m else float('inf')
            
            nums2_left_max = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right_min = nums2[j] if j < n else float('inf')
            
            # Valid partition found
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Odd case: return the larger left part element
                if total_len % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                # Even case: return the average of the two middle elements
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            # Move the binary search bounds
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
