class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
        # swap the values
        root.left, root.right = root.right, root.left

        # recursive call
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
