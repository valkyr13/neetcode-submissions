class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = defaultdict(list)
        num = 97

        for i in range(2,10):
            for j in range(3):
                char = chr(num)
                hm[i].append(char)
                num += 1
            if i == 7 or i == 9:
                hm[i].append(chr(num))
                num += 1
            print(hm[i])

        n = len(digits)
        res = []

        if len(digits) == 0:
            return []


        def helper(curr: [], digits:str, idx: int):
            if idx == n:
                res.append(("").join(curr))
                return

            for ch in hm[int(digits[idx])]:
                curr.append(ch)
                helper(curr, digits, idx+1)
                curr.pop()

        helper([], digits, 0)
        return res



        




        