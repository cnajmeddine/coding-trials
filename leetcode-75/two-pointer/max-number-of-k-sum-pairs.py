class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0
        for num in nums:
            target = k - num
            if count.get(target, 0) > 0:
                operations += 1
                count[target] -= 1
            else:
                count[num] = count.get(num, 0) + 1
        return operations
