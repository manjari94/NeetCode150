class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in t:
            if i not in s:
                return False
        return True
