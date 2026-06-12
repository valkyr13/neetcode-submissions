class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        l = 0
        r = k-1
        n = len(nums)

        diff = nums[r] - nums[l]

        while(r <n-1):
            l += 1
            r += 1
            diff = min(diff, nums[r] - nums[l])

        return diff

        

