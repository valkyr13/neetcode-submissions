class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        xor property

        """
        range_xor = 0
        nums_xor = 0
        for num in nums:
            nums_xor ^= num
        
        for i in range(len(nums)+1):
            range_xor ^= i


        return range_xor^nums_xor

        