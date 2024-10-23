class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1, return the string as it is
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to hold each row's characters
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string and place characters in the appropriate rows
        for char in s:
            rows[current_row] += char
            # Change direction when hitting the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move to the next row in the zigzag pattern
            current_row += 1 if going_down else -1
        
        # Join all the rows to get the final string
        return ''.join(rows)
