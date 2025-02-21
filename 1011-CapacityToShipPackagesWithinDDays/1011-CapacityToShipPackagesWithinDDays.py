class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)
        start = max(weights)
        end = sum(weights)
        while start < end:
            mid_capacity = (start + end) // 2
            days_temp = 1
            loaded = 0
            for w in weights:
                if loaded + w > mid_capacity:
                    loaded = w
                    days_temp+=1
                else:
                    loaded +=w
            if days_temp <= days:
                end = mid_capacity
            if days_temp > days:
                start = mid_capacity + 1

        return start 
                


                