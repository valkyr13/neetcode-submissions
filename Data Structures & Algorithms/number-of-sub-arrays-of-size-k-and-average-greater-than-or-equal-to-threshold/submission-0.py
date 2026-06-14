class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        l = 0
        s = 0

        for r in range(k):
            s += arr[r]
        
        target = k * threshold
        c = 0

        if s >= target:
            c += 1

        for r in range(k, n):
            s += arr[r]
            s -= arr[l]
            l += 1

            if s >= target:
                c += 1
        
        return c