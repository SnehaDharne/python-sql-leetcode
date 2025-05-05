class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i, 0) + 1
        val = hash_map[i]
        for key, value in hash_map.items():
            if value != val:
                return False
        return True
