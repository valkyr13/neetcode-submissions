class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        l = len(nums)

        for i in range(l):
            hm[nums[i]] = i
        
        ans = []
        for i in range(l):
            j = target - nums[i] 
            if j in hm and hm[j] != i:
                ans.append(i)
                ans.append(hm[j])
                return ans
        return ans
        