class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x, str_y = str(x), ''
        for i in range(len(str_x)):
            str_y += str_x[-(i+1)]
        return True if str_x == str_y else False
    
# Solution with just one line. By others users of LeetCode:
# print(str(x) == str(x)[::-1])