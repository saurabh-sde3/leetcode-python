## 342. Power of Four

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """      
        return n > 0 and (n&(n-1)) == 0 and len(str(bin(n))[2:]) % 2 == 1
    
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
    
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        arr = [1,4,16,64,256,1024,4096,16384,65536,262144,
               1048576,4194304,16777216,67108864,268435456,1073741824]
        return n in arr