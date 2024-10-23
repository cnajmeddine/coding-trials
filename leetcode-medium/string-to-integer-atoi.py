class Solution:
    def myAtoi(self, s: str) -> int:
        new_s = s.strip()
        the_num = ""
        num_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        
        # Check for empty string
        if not new_s:
            return 0
        
        # Initialize the starting index
        i = 0
        
        # Check for sign
        sign = 1
        if new_s[i] == '-':
            sign = -1
            i += 1
        elif new_s[i] == '+':
            i += 1
        
        # Construct the number
        while i < len(new_s) and new_s[i] in num_dict:
            the_num += new_s[i]
            i += 1
        
        # Convert the string to integer
        if the_num:
            num = sign * int(the_num)
            return max(min(num, 2**31 - 1), -(2**31))
        else:
            return 0

# Test the function
sol = Solution()
s = "   -42"
result = sol.myAtoi(s)
print(result)