class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ans = ""
        for s in strs:
            ans += "'"
            ans += s
        return ans
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.split("'")[1:]