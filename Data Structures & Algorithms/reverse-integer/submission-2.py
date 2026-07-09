class Solution:
    def reverse(self, x: int) -> int:
        digit = 0
        ans = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        int_max = (1 << 31) - 1

        while x != 0:
            digit = x%10
            x //= 10
            print(ans)
            if ans >= (int_max / 10):
                return 0
            ans = ans*10 + digit

        return ans*sign
        


            

        