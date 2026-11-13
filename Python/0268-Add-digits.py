class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:          # jab tak 2 ya zyada digits hain
            total = 0
            while num > 0:        # digits alag karke jodo
                total += num % 10 # last digit nikala
                num //= 10        # last digit hata diya
            num = total           # nayi sum ko num bana do
        return num