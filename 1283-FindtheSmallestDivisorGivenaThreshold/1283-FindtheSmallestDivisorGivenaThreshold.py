class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        ans = -1
        if sum(nums)<=threshold: return 1
        while start <= end:
            mid = (start + end)//2
            sum1 = 0
            for i in range(len(nums)):
                sum1+= math.ceil(nums[i]/mid)
            if sum1 <= threshold:
                ans = mid
                end = mid-1
            if sum1 > threshold:
                start = mid + 1
            

        return ans