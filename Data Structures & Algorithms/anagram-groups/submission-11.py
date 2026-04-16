class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        ans = []

        count = 0

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in hm:
                ans[hm[sorted_s]].append(s)
            else:
                hm[sorted_s] = count
                count += 1
                ans.append([s]) 
            
        return ans
            
        