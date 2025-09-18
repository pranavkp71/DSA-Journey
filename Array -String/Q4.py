# 125. Valid Palindrome

# Q) A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''.join(char for char in s if char.isalnum()).lower()
        reversed_string = cleaned_string[::-1]
        return cleaned_string == reversed_string

        




        



obj = Solution()
print(obj.isPalindrome(s="A man,  ,,,,plan, a canal: Panama"))