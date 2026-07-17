class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr = []
        ans = []
        n = len(candidates)

        def dfs(idx: int, target: int):
            if target == 0:
                ans.append(curr[:])
                return

            if idx == n or target < 0:
                return

            for i in range(idx,n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                dfs(i+1,target-candidates[i])
                curr.pop()
        
        dfs(0,target)
        return ans


        