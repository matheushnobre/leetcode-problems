class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ''
        for l in s:
            if l.isalpha() or l.isdecimal():
                string += l
        return string == string[::-1]