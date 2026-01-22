from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1

        for i in range(n2):
            freq2[ord(s2[i]) - ord('a')] += 1

            if i >= n1:
                freq2[ord(s2[i - n1]) - ord('a')] -= 1

            if freq1 == freq2:
                return True

        return False


        



obj = Solution()
print(obj.checkInclusion(s1='ab', s2="eidbaooo"))