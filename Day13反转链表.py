# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 击败95%
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        queue = collections.deque()
        node = head
        while node.next != None:
            queue.appendleft(node)
            node = node.next
        queue.appendleft(node)
        head = queue[0]
        prev = None
        for node in queue:
            if prev:
                prev.next = node
            prev = node
        node.next = None
        return head
