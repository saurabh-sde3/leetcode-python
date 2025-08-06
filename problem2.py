## 3479. Fruits Into Baskets III

class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        N = 1
        while N <= n:
            N <<= 1
        
        segTree = [0] * (2 * N)
        
        for i in range(n):
            segTree[N + i] = baskets[i]
        
        for i in range(N - 1, 0, -1):
            segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])
        
        count = 0
        for fruit in fruits:
            index = 1
            if segTree[index] < fruit:
                count += 1
                continue
            
            while index < N:
                if segTree[2 * index] >= fruit:
                    index = 2 * index
                else:
                    index = 2 * index + 1
            
            segTree[index] = -1
            while index > 1:
                index //= 2
                segTree[index] = max(segTree[2 * index], segTree[2 * index + 1])
        
        return count
    
fruits = [835,558,403,215,948,874,265,894,403,842,611,742,109,704,894,453,814,854,618,502,546,118,165,473,760,290,619,840,515]
baskets = [311,232,391,233,371,188,464,367,287,108,217,403,486,73,290,307,465,26,219,45,184,404,235,35,413,144,346,65,443]

print(Solution().numOfUnplacedFruits(fruits, baskets))