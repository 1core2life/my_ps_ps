# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.recursive(nums)
        
        
    
    
    def recursive(self, arr):
        res = TreeNode()
        if len(arr) != 0:
            big = self.get_big(arr)
            idx = arr.index(big)
            
            if big:
                res.val = big
            if idx is not 0:
                res.left = self.recursive(arr[:idx])
            if idx is not len(arr)-1:
                res.right = self.recursive(arr[idx+1:])
        
        return res
    
    
    def get_big(self, arr):
        res = 0
        for ar in arr:
            if res < ar:
                res = ar
            
        
        return res
