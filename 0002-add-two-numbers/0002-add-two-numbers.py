# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        r = 0
        while l1!=None or l2!=None or r!=0:
            val1 = 0
            val2 = 0
            if l1!=None:
                val1=l1.val
            if l2!=None:
                val2=l2.val
            cur.next = ListNode((val1+val2+r)%10)
            cur = cur.next
            r = (val1+val2+r)//10
            if l1 != None:
                l1 = l1.next
            if l2!=None: 
                l2 = l2.next
        return head.next