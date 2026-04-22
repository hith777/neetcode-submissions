class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        for i in range(len(s)):
            dict1[s[i]] = 1 + dict1.get(s[i], 0)
            dict1[t[i]] = -1 + dict1.get(t[i], 0)
        for v in dict1.values():
            if v != 0:
                return False
        return True