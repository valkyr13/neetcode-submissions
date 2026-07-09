class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = [0]*(len(num1)+ len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i])*int(num2[j])
                res[i+j] += digit
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10
        

        res = res[::-1]
        ans = ""
        for i in range(len(res)):
            if res[i] != 0:
                break
        
        for j in range(i,len(res)):
            ans += str(res[j])
        return ans
            
        