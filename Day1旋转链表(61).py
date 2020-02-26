class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return []
        l = 1
        node = head
        while node.next:
            node = node.next
            l += 1
        node.next = head
        m = k % l
        for i in range(l-m):
            node = node.next
        head = node.next
        node.next = None
        return head
