
from collections import Counter 


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        bucket sort
        """
        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        freqDict = Counter(nums)

        for x,y in freqDict.items():
            bucket[y].append(x)
        """
        1, 2, 3. .... 5
         
        """
        ans = []
        for i in range(n,0,-1):
            print(i)
            print(bucket[i])
            if k == 0:
                break
            if len(bucket[i]) != 0:
                for j in range(len(bucket[i])):
                    if k == 0:
                        break
                    ans.append(bucket[i][j])
                    k -= 1
        return ans
                

                


            
        