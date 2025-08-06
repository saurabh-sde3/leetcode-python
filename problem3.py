## 314. Binary Tree Vertical Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root):
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]

# write driver code to test the function
if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree for testing
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Create an instance of the Solution class
    solution = Solution()
    # Call the verticalOrder function and print the result
    print(solution.verticalOrder(root))