class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Binary Search Answers

        start = 1
        end = max(piles)
        ans = 0
        while start <=  end:
            mid = (start + end) //2
            sum1 = 0
            for i in range(len(piles)):
                sum1 += math.ceil(piles[i] /mid)
            
            if sum1 <= h:
                ans = mid
                end = mid - 1 
            else:
                start = mid + 1
        

        return ans

