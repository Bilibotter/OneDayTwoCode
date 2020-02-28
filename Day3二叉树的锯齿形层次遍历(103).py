class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        left = True
        prev = [root]
        while prev:
            temp = []
            n = []
            for tree in prev:
                temp.append(tree.val)
                if tree.left:
                    n.append(tree.left)
                if tree.right:
                    n.append(tree.right)
            if left:
                res.append(temp)
            else:
                res.append(temp[::-1])
            left = not left
            prev = n
        return res
