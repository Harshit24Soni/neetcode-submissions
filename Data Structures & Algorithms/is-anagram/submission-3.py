class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seens = {}
        seent = {}

        for char in s:
            if char in seens:
                seens[char] += 1
            else:
                seens[char] = 1

        for char in t:
            if char in seent:
                seent[char] += 1
            else:
                seent[char] = 1

        return seens == seent