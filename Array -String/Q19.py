# 344. Reverse String

# Q) Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def reverseString(self, s) -> None:
        j = len(s) - 1
        for i in range(len(s)//2):
            if i != j:
                s[i], s[j] = s[j], s[i]
                j -= 1
                print(s)



obj = Solution()
obj.reverseString(s=["h","e","l","l","o"])
        