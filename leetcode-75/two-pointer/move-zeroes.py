class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroIndex] = nums[zeroIndex], nums[i]
                zeroIndex += 1