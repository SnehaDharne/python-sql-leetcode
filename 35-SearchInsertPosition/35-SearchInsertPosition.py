class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        if target > nums[end]:
            return end+1
        if target < nums[start]:
            print('target is less than start')
            return 0
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        while start <= end:
            mid = int(start + ((end-start)/2))
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid+1
            if nums[mid] > target:
                end = mid-1
        
        return start