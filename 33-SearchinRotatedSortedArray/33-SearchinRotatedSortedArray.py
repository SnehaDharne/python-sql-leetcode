class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            mid = int(start + (end-start) /2)
            if nums[mid] == target:
                return mid
            1234560-1
            #left half is sorted
            if nums[start] < nums[mid]:
                if nums[start] < target and target <= nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            #right sorted
            else:
                if nums[end] > target and target >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        
        return -1