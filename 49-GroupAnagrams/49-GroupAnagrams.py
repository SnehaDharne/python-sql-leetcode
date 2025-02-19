class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in my_map:
                my_map[sorted_str].append(strs[i])
            else:
                my_map[sorted_str] = [strs[i]]
        results = []
        for key, value in my_map.items():
            results.append(value)
        
        return results
        