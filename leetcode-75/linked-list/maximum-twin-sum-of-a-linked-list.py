class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        current = head
        
        # Collect values from the list
        while current:
            values.append(current.val)
            current = current.next
            
        max_twin_sum = 0
        n = len(values)
        
        # Calculate twin sums and track the maximum
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_twin_sum = max(max_twin_sum, twin_sum)
        
        return max_twin_sum
