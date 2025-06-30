class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        while n != 1:
            m = str(n)
            sum1 = 0
            for num in m:
                sum1 += int(num) * int(num)
            if sum1 in hash_set:
                return False
            else:
                hash_set.add(sum1)
            n = sum1

        return True
