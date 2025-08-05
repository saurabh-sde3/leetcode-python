## 3477. Fruits Into Baskets II

class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        count = 0
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[i] = 0
                    break
            else:
                count += 1
        return count
    
print(Solution().numOfUnplacedFruits([4,2,5], [3,5,4]))