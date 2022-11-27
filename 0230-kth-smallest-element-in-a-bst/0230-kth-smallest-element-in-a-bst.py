# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l1 = []
        n=0
        cur = root
        
        while cur or l1:
            while cur:
                l1.append(cur)
                cur = cur.left
            cur = l1.pop()
            n+=1
            if n==k:
                return cur.val
            cur =cur.right
            