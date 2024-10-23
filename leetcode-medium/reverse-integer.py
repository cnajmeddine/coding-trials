class Solution:
    def reverse(self, x: int) -> int:
        # Define the bounds for 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Initialize result and handle negative sign
        result = 0
        negative = x < 0
        x = abs(x)
        
        while x != 0:
            # Get the last digit of the number
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying result by 10
            if result > (INT_MAX - digit) // 10:
                return 0  # Return 0 if overflow would occur
            
            result = result * 10 + digit
        
        return -result if negative else result
