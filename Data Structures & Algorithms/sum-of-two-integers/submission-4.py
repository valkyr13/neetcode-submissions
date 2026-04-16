class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        left - right
        1 + 1  01
        1 + 0 = 1
        0 + 1 = 1

        get bit

        a ^ b  = a
        a & b << 1  = carry = b

        negative number?

        """
        # 2^31-1

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        carry = 0

        while b != 0:
            carry = (a & b) << 1
            a = (a^b) & mask
            b = carry & mask


        return a if a <=max_int else ~(a^mask)

                    

                
        