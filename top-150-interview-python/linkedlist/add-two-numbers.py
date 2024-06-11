from typing import Optional

# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = ''
        
        while l1 != None:
            n1 += str(l1.val)
            l1 = l1.next
            
        while l2 != None:
            n2 += str(l2.val)
            l2 = l2.next

        sum = str(int(n1[::-1]) + int(n2[::-1]))[::-1]
        l3 = ListNode(int(sum[0]))
        
        for index in range(1, len(sum)):
            digit = sum[index]
            pointer = l3
            while(pointer.next):
                pointer = pointer.next
            pointer.next = ListNode(int(digit))
                    
        return l3