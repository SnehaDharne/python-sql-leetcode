class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums_Set = set(nums)
        ns = len(nums_Set)
        lcs = 1
        if nums == []:
            return 0
        if n == 1:
            return 1
        for item in nums_Set:
            if item-1 not in nums_Set:
                seq = 1
                num = item
                while (num+1 in nums_Set):
                    seq +=1
                    num+=1
                    lcs = max(lcs, seq)

        return lcs

                
