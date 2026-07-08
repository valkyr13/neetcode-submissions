class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.hm.get(key,[])
        if len(val) == 0 :
            self.hm[key] = [[value, timestamp]]
        else:
            val.append([value, timestamp])
            self.hm[key] = val
        
    def get(self, key: str, timestamp: int) -> str:
        val = self.hm.get(key,[])
        if len(val) == 0:
            return ""
        else:
            j = len(self.hm[key]) - 1
            i = 0
            ans = ""
            while(i<=j):
                mid = (i+j)//2
                if self.hm[key][mid][1] < timestamp:
                    ans = self.hm[key][mid][0]
                    i = mid + 1
                elif self.hm[key][mid][1] > timestamp :
                    j = mid-1
                else:
                    return self.hm[key][mid][0]

            return ans
            
        
