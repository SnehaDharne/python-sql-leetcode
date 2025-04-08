# Last updated: 4/7/2025, 8:22:01 PM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        i = 0
        j = len(height) -1

        while i < j:
                vol = min(height[i],height[j]) * (j-i)
                max_vol = max(vol, max_vol)
                if height[i] < height[j]:
                    i +=1
                else:
                    j -=1
        
        return max_vol