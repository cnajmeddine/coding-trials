class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    
        # Check if the string matches the pattern
        return bool(re.match(pattern, s.strip()))