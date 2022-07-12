# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
子树的子树也包含在内
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = collections.defaultdict(int)
        ans = []
        def dfs(node):
            if node == None:
                return "|"
            uid = f"{node.val} {dfs(node.left)} {dfs(node.right)}"
            if dic[uid] == 1:
                ans.append(node)
            dic[uid] += 1
            return uid
        dfs(root)
        return ans