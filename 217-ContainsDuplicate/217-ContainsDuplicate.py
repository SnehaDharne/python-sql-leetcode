class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        diff = len(nums) - len(nums_set)
        if diff > 0:
            return True
        else:
            return False