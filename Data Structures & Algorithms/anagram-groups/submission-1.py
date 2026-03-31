class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in strs:
            sorted_value="".join(sorted(i))
            a[sorted_value].append(i)
        return list(a.values())