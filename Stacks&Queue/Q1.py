# 20. Valid Parentheses

# Q) Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[char]:
                        return False
        
        return not stack
    


obj = Solution()
print(obj.isValid(s='(([]))'))