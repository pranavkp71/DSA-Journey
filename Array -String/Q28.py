# 3. Longest Substring Without Repeating Characters

# Q) Given a string s, find the length of the longest substring without duplicate characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        sett = set()
        max_length = 0

        for R in range(len(s)):
            while s[R] in sett:
                sett.remove(s[L])
                L += 1
            
            sett.add(s[R])

            max_length = max(max_length, R-L+1)
        return max_length



obj = Solution()
print(obj.lengthOfLongestSubstring(s="abcabc"))