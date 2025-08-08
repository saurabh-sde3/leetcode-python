# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Compute the tree's height via recursion
    def height(self, root):
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        abs_height = abs(left_height - right_height)
        return (
            abs_height < 2
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )
        
# write driver code to test the function
if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree for testing
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()

    # Check if the constructed tree is balanced
    print(solution.isBalanced(root))  # Output: True
    
    