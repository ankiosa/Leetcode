# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    
    def addTwoNumbers_func(self, l1, l2, part_sum, n):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1):
            print(l1.val)

        if(l1 and l2):
            sum_val = part_sum+l1.val+l2.val
        elif(l1):
            sum_val = part_sum+l1.val
        elif(l2):
            sum_val = part_sum+l2.val
        else:
            if(part_sum==1):
                sum_val = part_sum
                n.next = ListNode(sum_val)
                n = n.next
            return n
        print(sum_val)
        if(sum_val>=10):
            part_sum=1
            sum_val -= 10
        else:
            part_sum=0
        n.next = ListNode(sum_val)
        n = n.next
        
        if(l1 and l2):
            return self.addTwoNumbers_func(l1.next, l2.next, part_sum, n)
        elif(l1):
            return self.addTwoNumbers_func(l1.next, None, part_sum, n)
        elif(l2):
            return self.addTwoNumbers_func(None, l2.next, part_sum, n)
        else:
            return self.addTwoNumbers_func(None, None, part_sum, n)

        
    
    
    
    def addTwoNumbers(self, l1, l2, part_sum=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root =n = ListNode(0)
        self.addTwoNumbers_func(l1, l2, part_sum, n)
        print(root)
        return root.next
        