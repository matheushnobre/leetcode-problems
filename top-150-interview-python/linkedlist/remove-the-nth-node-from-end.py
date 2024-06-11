from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux = head
        pointer = head
        for i in range(n):
            if pointer.next:
                pointer = pointer.next
            else:
                return head.next
                
        while pointer.next:
            aux = aux.next
            pointer = pointer.next
            
        aux.next = aux.next.next

        return head