class Solution:
    def isHappy(self, n: int) -> bool:
        self.storage = set()

        def helper(n: int) -> bool:
            sum = 0
            while(n > 0):
                sum += (n%10)**2
                n = n//10

            if sum == 1:
                return True
            elif sum in self.storage:
                return False
            self.storage.add(sum)
            return helper(sum)

        return helper(n)



        



        
        