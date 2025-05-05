class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i, 0) + 1
        val = hash_map[i]
        all_vals = hash_map.values()
        return len(set(all_vals)) == 1
