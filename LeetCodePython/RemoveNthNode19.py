# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None
        currentHead = head
        currentFinish = head
        for k in range(n + 1):
            currentFinish = currentFinish.next
        while currentFinish.next != None:
            currentFinish = currentFinish.next
            currentHead = currentHead.next
        currentHead.next=currentHead.next.next
        return currentHead
