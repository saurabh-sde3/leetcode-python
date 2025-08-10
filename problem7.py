## 869. Reordered Power of 2

from collections import Counter
class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        counter = Counter(str(n))
        for i in range(32):
            num = 1 << i
            if Counter(str(num)) == counter:
                return True
        return False

    # def reorderedPowerOf2(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     li = list(permutations(str(n)))
    #     for item in li:
    #         if item[0] == '0':
    #             continue
    #         num = int(''.join(list(item)))
    #         if (num & num - 1) == 0:
    #             return True
    #     return False

print(Solution().reorderedPowerOf2(45))  # Example test case