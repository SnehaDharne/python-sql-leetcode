class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[start] == target:
                return True
            if nums[end] == target:
                return True

            mid = int(start + (end-start) /2)
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid] and nums[mid] == nums[end]:
                start += 1
                end -= 1
                continue
            elif nums[start] == nums[mid]:
                start +=1
            elif nums[mid] == nums[end]:
                end -=1
            #left half is sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            #right sorted
            else:
                if nums[end] >= target and target >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        
        return False