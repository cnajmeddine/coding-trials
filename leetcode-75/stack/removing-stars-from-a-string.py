class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()  # Remove the closest non-star character
            else:
                stack.append(char)  # Add non-star character to the stack
        return ''.join(stack)  # Join the characters in the stack to form the result
