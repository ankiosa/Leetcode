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
        if(head.next==None):
            return None
        counter = 0
        root = head
        while(head!=None):
            head = head.next
            counter += 1
        n_start = max(n-counter,counter-n)
        
        counter =0
        head = root
        root = head
        print(n_start)
        if(n_start==0):
            head.val = head.next.val
            head.next = head.next.next
            return root
        while(counter<n_start-1):
            head = head.next
            counter += 1
        print(head.val)
        if(head.next.next==None):
            head.next=None
            print("ok1")
        else:
            head = head.next
            head.val = head.next.val
            head.next = head.next.next
            print("ok2")
        return root
                
        
        