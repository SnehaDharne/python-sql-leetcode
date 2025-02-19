class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k*m:
            return -1
        start = min(bloomDay)
        end = max(bloomDay)
        print(start, end)
        while start <= end:
            mid = (start + end) //2
            count = 0
            bouq = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    count +=1
                else:
                    bouq += count // k
                    count = 0

            bouq += count // k

            if bouq >= m:
                end = mid - 1
            else:
                start = mid + 1
                
        return start