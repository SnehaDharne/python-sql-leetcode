# Last updated: 4/5/2025, 5:34:30 PM
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count_map = {}
        for i in arr:
            if i not in count_map:
                count_map[i] = 1
            else:
                count_map[i] +=1
        
        l1 = list(count_map.values())

        return (len(l1) == len(set(l1)))
        