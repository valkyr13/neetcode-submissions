class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1 = len(s1) - 1

        l2 = len(s2) - 1

        if l1 > l2:
            return False

        hm = {}
        m = {}

        for i in range(len(s1)):
            hm[s1[i]] = hm.get(s1[i], 0) + 1

            
        for i in range(len(s1)):
            if hm.get(s2[i], 0) != 0:
                m[s2[i]] = m.get(s2[i], 0) + 1

        i = 0
        j = l1
        print(hm)
        print(m)

        while j <= l2:
            print("i: ",i,"j: ",j,"m: ",m)

            if hm == m:
                return True

            f = m.get(s2[i], 0)

            if f != 0:
                m[s2[i]] = f - 1
                
                if m[s2[i]] == 0:
                    del m[s2[i]]

            i += 1

            j += 1

            if j <= l2 and hm.get(s2[j], 0) != 0:
                m[s2[j]] = m.get(s2[j], 0) + 1
        

        return False
