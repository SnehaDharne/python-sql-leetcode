class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #bruteforce
        # triplets = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 trip = [nums[i], nums[j], nums[k]]
        #                 trip.sort()
        #                 if trip not in triplets:
        #                     triplets.append(trip)
        
        # return triplets
        #two loops

        # triplets = []
        # for i in range(len(nums)):
        #     my_hash_set = set()
        #     for j in range(i+1, len(nums)):
        #         if -(nums[i] + nums[j]) in my_hash_set:
        #             my_trip = [nums[i], nums[j], -(nums[i]+nums[j])]
        #             my_trip.sort()
        #             if my_trip not in triplets:
        #                 triplets.append(my_trip)
                
        #         my_hash_set.add(nums[j])
        # return triplets

        #two pointer
        target = 0
        nums.sort()
        s = set()
        triplets = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        triplets = list(s)


                    
        
        return triplets