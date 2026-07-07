class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        arr.sort()

        current = head
        i = 0
        while current:
            current.val = arr[i]
            i += 1
            current = current.next

        return head
