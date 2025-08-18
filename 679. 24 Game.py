class Solution:
    def judgePoint24(self, cards):
        EPS = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])
    
    
class Solution2:
    # All possible operations we can perform on two numbers.
    def generate_possible_results(self, a: float, b: float) -> List[float]:
        res = [a + b, a - b, b - a, a * b]
        if a:
            res.append(b / a)
        if b:
            res.append(a / b)  
        return res
    
    # Check if using current list we can react result 24.
    def check_if_result_reached(self, cards: List[float]) -> bool:
        # Base Case: We have only one number left, check if it is approximately 24.
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.1

        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                # Create a new list with the remaining numbers and the new result.
                new_list = [number for k, number in enumerate(cards) if (k != i and k != j)]
                
                # For any two numbers in our list, we perform every operation one by one.
                for res in self.generate_possible_results(cards[i], cards[j]):
                    # Add the new result to the list.
                    new_list.append(res)
                    
                    # Check if using this new list we can obtain the result 24.
                    if self.check_if_result_reached(new_list):
                        return True
                    
                    # Backtrack: remove the result from the list.
                    new_list.pop()
                    
        return False
    
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.check_if_result_reached(cards)