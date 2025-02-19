class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        print(words)
        if len(words) == 1:
            return s
        words = words[::-1]
        res = [i for i in words if i != ''] 
        ans = " ".join(res)
        return ans