class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        if x == 0:
            return 0
        if x < 0:
            return 0

        start = 1
        end = x

        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1

        return end
            
        
            
