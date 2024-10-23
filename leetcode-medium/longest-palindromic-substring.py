class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Function to expand around the center and return the longest palindrome
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome found by expanding
            return s[left + 1:right]

        # Initialize an empty string for the longest palindrome
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Check for odd-length palindromes (centered at one character)
            odd_palindrome = expandAroundCenter(i, i)
            # Check for even-length palindromes (centered at two characters)
            even_palindrome = expandAroundCenter(i, i + 1)
            
            # Update the longest palindrome if found longer one
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
        
        return longest_palindrome
