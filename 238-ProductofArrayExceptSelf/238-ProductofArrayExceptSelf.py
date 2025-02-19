class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0: zero_count +=1
        answer = []
        if zero_count < 2 :
            for i in range(len(nums)):
                if nums[i] != 0:
                    product = product * nums[i]
            if 0 in nums:
                for i in range(len(nums)):
                    if nums[i] != 0:
                        answer.append(0)
                    else:
                        answer.append(product)
            else:

                for i in range(len(nums)):
                    if nums[i]!=0:
                        answer.append(int(product/nums[i]))
                    else:
                        answer.append(int(product))
        if zero_count > 1:
            answer = [0]*len(nums)
            
        return answer