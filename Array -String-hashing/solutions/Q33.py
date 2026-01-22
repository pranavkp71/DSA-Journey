class Solution:
    def totalFruit(self, fruits) -> int:
        basket = {}
        L = 0
        max_len = 0
        for R in range(len(fruits)):
            fruit = fruits[R]

            if fruit in basket:
                basket[fruit] += 1
            else:
                basket[fruit] = 1

            while len(basket) > 2:
                left_fruit = fruits[L]
                basket[left_fruit] -= 1

                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                
                L += 1

            max_len = max(max_len, R-L+1)
        
        return max_len




obj = Solution()
print(obj.totalFruit(fruits = [0,1,2,2]))