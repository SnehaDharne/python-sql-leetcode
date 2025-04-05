# Last updated: 4/5/2025, 5:41:30 PM
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1_map = {}
        word2_map = {}
        for char in word1:
            word1_map[char] = word1_map.get(char,0)+1
        for char in word2:
            word2_map[char] = word2_map.get(char,0)+1
        
        if set(word1_map.keys()) != set(word2_map.keys()):
            return False

        return sorted(word1_map.values()) == sorted(word2_map.values())



        