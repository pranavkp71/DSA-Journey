# 1768. Merge Strings Alternately

# Q) You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        A, B = len(word1), len(word2)
        a = b = 0

        word = 1

        while a < A and b < B:
            if word == 1:
                merged.append(word1[a])
                a += 1
                word = 2
            else:
                merged.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            merged.append(word1[a])
            a += 1
        
        while b < B:
            merged.append(word2[b])
            b += 1

        return ''.join(merged)





obj = Solution()
print(obj.mergeAlternately(word1='abc', word2='pqr'))