class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        map = {}

        for i in range(n):
            curr = "".join(sorted(strs[i]))

            if curr not in map:
                map[curr] = []
            map[curr].append(strs[i])
        

        return list(map.values())