class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_pairs = {')': '(', ']': '[', '}': '{'} 

        for char in s: 
            if char in '([{': 
                stack.append(char) 
            elif char in ')]}': 
                if not stack: 
                    return False
                top_element = stack.pop()
                if matching_pairs[char] != top_element: 
                    return False

        return not stack 

            