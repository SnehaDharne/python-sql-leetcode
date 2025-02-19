def check_num(num):
    number = int(num[-1])
    if number % 2 != 0:
        return True
    else:
        return False
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            ans = check_num((num[:i+1]))
            if ans:
                return num[:i+1]
            else:
                continue

        return ""
