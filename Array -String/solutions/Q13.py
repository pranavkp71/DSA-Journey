# 242. Valid Anagram

# Q) Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        
        for char in s:
            if s.count(char) != t.count(char):
                return False
        return True
                

        

        
obj = Solution()
print(obj.isAnagram(s="anagram", t = "nagaram"))