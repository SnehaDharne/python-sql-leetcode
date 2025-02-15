import sys
max_int = sys.maxsize
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        min_num = max_int
        if len(nums) == 1:
            return nums[0]
        while start <= end:
            mid = (start + end)//2

            if nums[start] <= nums[mid]:
                min_num = min(nums[start], min_num)
                start = mid+1
            else:
                min_num = min(nums[mid], min_num)
                end = mid - 1
        
        return min_num
