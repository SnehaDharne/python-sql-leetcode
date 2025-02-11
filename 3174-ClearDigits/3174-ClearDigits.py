class Solution:
    def clearDigits(self, s: str) -> str:
        index = 0
        
        while index < len(s):
            if s[index].isdigit():
                s = s[:index] + s[index+1:]
                
                if index > 0:
                    s = s[:index-1] + s[index:]
                    index -= 1
            else:
                index += 1
        
        return s