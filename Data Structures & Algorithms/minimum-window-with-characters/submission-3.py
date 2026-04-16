class Solution:
    def helper(self,s1: [], s2: [])-> bool:
        for k, v in s1.items():
            f = s2.get(k,0)
            if f < v:
                return False
        return True
            
    def minWindow(self, s: str, t: str) -> str:
        subMap = dict()
        strMap = dict()

        for i in range(len(t)):
            f = subMap.get(t[i],0)
            subMap[t[i]] = f + 1

        i = 0
        n = len(s)
        m = float('inf')
        sub = ""
        for j in range(len(s)):
            f2 = subMap.get(s[j],0)

            if f2 != 0:
                f1 = strMap.get(s[j],0)
                strMap[s[j]] = f1+1

                # reduce size
                while (i < n and self.helper(subMap, strMap)):
                    if j-i+1 < m:
                        sub = s[i:j+1]
                        m = j-i+1

                    if s[i] in strMap:
                        strMap[s[i]] -= 1
                    i += 1 

        return sub