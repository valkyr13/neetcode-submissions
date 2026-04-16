class Solution:
    def trap(self, height: List[int]) -> int:
        """
        water at any point = min(max height in surroundings)- height at i
        """
        l = 0
        r = len(height)-1

        t = 0

        lmax = height[l]
        rmax = height[r]

        l += 1
        r -= 1 

        while(l<=r):
            if lmax < rmax:
                delta = lmax - height[l]
                lmax = max(lmax, height[l])
                l += 1
            else:
                delta = rmax - height[r]
                rmax = max(rmax, height[r])
                r -= 1
            if delta > 0:
                    t += delta
        return t
        