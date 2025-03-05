class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # num = str(x)
        # if len(num) == 1:
        #     return True
        # i=0
        # j=len(num) -1
        # while i<j:
        #     if num[i] != num[j]:
        #         return False
        #     i+=1
        #     j-=1

        return str(x) == str(x)[::-1]