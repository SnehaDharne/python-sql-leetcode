class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        start = 1
        end = max(nums)
        ans = -1
        if sum(nums)<=threshold: return 1
        while start <= end:
            print(start, 'start')
            print(end, 'end')
            mid = (start + end)//2
            print(mid, 'mid')
            sum1 = 0
            for i in range(n):
                sum1+= math.ceil(nums[i]/mid)
            if sum1 <= threshold:
                ans = mid
                end = mid-1
            if sum1 > threshold:
                start = mid + 1
            

        return ans