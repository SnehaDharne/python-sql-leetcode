class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ''
        for i in range(min(len(word1), len(word2))):
            res+=word1[i]
            res+=word2[i]
        if len(word1) == len(word2):
            return res
        if i == len(word1)-1:
            res+=word2[i+1:]
        if i == len(word2)-1:
            res+=word1[i+1:]

        return res

