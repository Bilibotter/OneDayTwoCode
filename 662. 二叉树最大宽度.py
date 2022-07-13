# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = collections.defaultdict(list)
        def dfs(i, j ,node):
            if not node:
                return
            dic[i].append(j)
            if node.left:
                dfs(i+1, j*2+1, node.left)
            if node.right:
                dfs(i+1, j*2+2, node.right)
        dfs(0, 0, root)
        maxn = 0
        for v in dic.values():
            if len(v) <= 1:
                maxn = max(len(v), maxn)
            else:
                maxn = max(v[-1]-v[0]+1, maxn)
        return maxn
