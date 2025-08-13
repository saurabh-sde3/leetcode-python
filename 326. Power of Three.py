class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hp = 1162261467
        if n <= 0:
            return False

        if hp % n == 0:
            return True
        return False