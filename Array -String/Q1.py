# 1768. Merge Strings Alternately

# Q) You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0

        while i < m and j < n:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        
        if i < m:
            merged.append(word1[i:])
        if j < n:
            merged.append(word2[j:])
            
        return "".join(merged)
        
                         


obj = Solution()
print(obj.mergeAlternately("abc", "pqr"))
