class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        n = len(nums)
        ans = []
        curr = []

        def helper(s: set, i: int, curr: List[int]):
            if i == n:
                ans.append(curr[:])
                return

            for num in list(s):
                    curr.append(num)
                    s.remove(num)
                    helper(s,i+1,curr)
                    curr.pop()
                    s.add(num)

        helper(s, 0, [])
        return ans
