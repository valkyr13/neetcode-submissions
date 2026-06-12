class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        so i need a subarray whre first and last el are equal and diff is <=k
        
        brute force
        i have to go through all the subarrays - o()
        fixed length = k 
        
        r++ and check window size
        is there duplicate at index r -> check map

        window == k 
        l ++
        remove l-1 from map

        boundary
          l = n-1
            return
        

        """
        visited = set()
        n = len(nums)
        r = 0
        l = 0


        while(r < n):
            if nums[r] in visited:
                return True
            visited.add(nums[r])
            if r-l >= k:
                visited.remove(nums[l])
                l += 1
            r += 1
            
        
        return False



            



        