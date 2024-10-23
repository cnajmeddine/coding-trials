class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_index = {}
        
        # Initialize start of window, max length
        start = 0
        max_length = 0
        
        # Loop through the string
        for i, char in enumerate(s):
            # If character is found in the dictionary and is within the current window
            if char in char_index and char_index[char] >= start:
                # Move the start to the right of the last occurrence of char
                start = char_index[char] + 1
            
            # Update the last seen index of the character
            char_index[char] = i
            
            # Calculate the max length of the current window
            max_length = max(max_length, i - start + 1)
        
        return max_length
