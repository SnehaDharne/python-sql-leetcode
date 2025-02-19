class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1
        my_map = sorted(my_map.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in my_map[:k]]
