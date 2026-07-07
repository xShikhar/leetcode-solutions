class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        if prev is None:
            return None

        prev.next = slow.next

        return head
