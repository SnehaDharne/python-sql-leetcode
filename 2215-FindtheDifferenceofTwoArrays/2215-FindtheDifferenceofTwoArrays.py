# Last updated: 4/5/2025, 6:09:13 PM
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = list(s[::-1])  # Convert to a list for mutable modification
        s_count = 0
        for i in range(len(s1)):
            if s1[i] == '*':
                s1[i] = '' 
                s_count += 1
            elif s_count > 0:
                s1[i] = '' 
                s_count -= 1
        return "".join(s1)[::-1]
