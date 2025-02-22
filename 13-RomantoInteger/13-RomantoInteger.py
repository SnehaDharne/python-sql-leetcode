class Solution:
    def romanToInt(self, s: str) -> int:
        my_map = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        val = 0
        i=0
        while i<len(s):
            if i + 1 < len(s) and s[i+1] in ['V','L','D','X','C','M'] and s[i] in ['I','X','C'] and my_map[s[i+1]] > my_map[s[i]]:
                val = val - my_map[s[i]] + my_map[s[i+1]]
                i=i+2
            else:
                val = val + my_map[s[i]]
                i = i+1

           

        return val