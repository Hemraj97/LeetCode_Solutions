#https://leetcode.com/problems/group-anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map = dict()
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in res_map.keys():
                res_map[sorted_str] = res_map[sorted_str] + [strs[i]]
            else:
                res_map[sorted_str] = [strs[i]]
        result = list()
        for k,v in res_map.items():
            result.append(v)
        if result:
            return result
        else:
            return [[""]]