
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            self.res = max(self.res, l + r + 1)
            return max(l, r) + 1

        helper(root)
        return self.res - 1


