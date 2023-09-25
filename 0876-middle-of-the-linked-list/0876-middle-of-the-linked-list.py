# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # first = head
        # while head and head.next:
        #     second = first.next
        #     head = head.next.next
        # return second
        
        
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head