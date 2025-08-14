## 2264. Largest 3-Same-Digit Number in String

class Solution(object):
    def largestGoodInteger(self, num):
        for i in reversed(range(10)):
            substring = str(i)*3
            if substring in num:
                return substring
        return ""