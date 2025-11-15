# 9. Palindrome Number

# Q) Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = str(x)
        List = list(value)
        Revered = List[::-1]
        if List == Revered:
            return True
        else:
            return False

    
obj = Solution()
print(obj.isPalindrome(-121))



