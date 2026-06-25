class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two pointer approach
        one at smallest el, other at biggest el
        increase or decrese depending on the sum is greater than or less than target
        
        """

        p1 = 0
        p2 = len(numbers)-1


        while(p1<p2):
            curr = numbers[p1]+ numbers[p2]
            if curr == target:
                return [p1+1,p2+1]
            elif curr < target:
                p1 += 1
            else:
                p2 -= 1

        return []
        