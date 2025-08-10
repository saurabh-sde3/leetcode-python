## 257. Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        op = []
        def paths(root, st=""):
            if root is None:
                return
            st = st + str(root.val) + "->"
            if root.left == None and root.right == None:
                op.append(st[:-2])
                st = ""
            paths(root.left, st)
            paths(root.right, st)
        paths(root)
        return op
    
'''
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''