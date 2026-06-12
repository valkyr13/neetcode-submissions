class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        contiuous subarray
        fixed length type
        """

        l = 0
        r = 0
        n = len(blocks)
        c = 0
        minc = k

        while(r <n):
            if blocks[r] == 'W':
                c += 1
            
            if r-l+1 == k:
                minc = min(c,minc)
                if blocks[l] == 'W':
                        c -= 1
                l += 1
            r += 1
            

        return minc

        