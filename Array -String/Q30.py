class Solution:
    def characterReplacement(self, s, k) -> int:
        freq = {}        
        L = 0
        max_freq = 0     
        max_len = 0

        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1
            
            max_freq = max(max_freq, freq[s[R]])

            while (R - L + 1) - max_freq > k:
                freq[s[L]] -= 1
                L += 1
            
            max_len = max(max_len, R - L + 1)
        
        return max_len
        
        












obj = Solution()
print(obj.characterReplacement(s = "AABABBA", k = 1))