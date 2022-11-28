# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        print("res: ", res, "\n ##########")
        
        def dfs(root):
            if not root:
                return 0
            
            leftmax = max(dfs(root.left), 0)
            print("printing LeftMax:  ", leftmax)
            rightmax= max(dfs(root.right), 0)
            print("printing rightMax:  ", rightmax)
            
            res[0] = max(res[0], root.val + leftmax +rightmax)
            print("Printing res after calculation: ", res)
            print("\n $$$$$$$$")
            print(root.val + max(leftmax, rightmax))
            
            return root.val + max(leftmax, rightmax)
        dfs(root)
        
        return res[0]
            
            
        