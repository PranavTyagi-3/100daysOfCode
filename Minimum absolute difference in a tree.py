# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        li=[]
        def func(root):
            if root is None:
                return
            li.append(root.val)
            func(root.right)
            func(root.left)

        func(root)

        li.sort()
        m=10e5
        for i in range(1,len(li)):
            v=abs(li[i]-li[i-1])
            if v<m:
                m=v

        return m