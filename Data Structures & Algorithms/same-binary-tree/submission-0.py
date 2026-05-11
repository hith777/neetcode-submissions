# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def serialize(node, res):
            if not node:
                res.append("N")
                return res
            
            res.append("$" + str(node.val))
            serialize(node.left, res)
            serialize(node.right, res)

            return res
        
        ps = "".join(serialize(p, []))
        qs = "".join(serialize(q, []))

        return ps == qs