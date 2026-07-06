class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        factor = 1
        num = 0

        for i in range(len(digits)-1,-1,-1):
            num += factor*digits[i]
            factor *= 10
        num += 1

        while(num>0):
            res.append(num%10)
            num //= 10
        return res[::-1]


        