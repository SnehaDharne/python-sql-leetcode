
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0]>nums[1]:
                return 0
            elif nums[0] < nums[1]:
                return 1
            else:
                return -1
        if nums[start] > nums[start+1]:
            return start
        if nums[end-1] > nums[end-2]:
            return end-1
        while start < end:
            mid = (start + end) // 2
            print(mid)
            if nums[mid-1] < nums[mid] and nums[mid +1] < nums[mid]:
                return mid
            if nums[mid-1]<nums[mid] and nums[mid] < nums[mid+1]:
                start = mid
            if nums[mid-1]>nums[mid] and nums[mid]>nums[mid+1]:
                end = mid 
            if nums[mid-1] > nums[mid] and nums[mid]<nums[mid+1]:
                end = mid
            

        return -1