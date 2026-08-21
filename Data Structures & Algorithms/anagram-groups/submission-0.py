class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            sort_str = ''.join(sorted(i))
            if sort_str in hash_map :
                hash_map[sort_str].append(i)
            else:
                hash_map[sort_str] = [i]
        return(list(hash_map.values()))


        