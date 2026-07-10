class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def findNode(node, k):
            for _ in range(k - 1):
                node = node.next
                if not node:
                    return None
            return node

        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

        temp = head
        prevNode = None          

        while temp:
            kthnode = findNode(temp, k)

            if kthnode == None:
                if prevNode:
                    prevNode.next = temp   
                break

            nextNode = kthnode.next
            kthnode.next = None

            reverse(temp)

            if temp == head:
                head = kthnode
            else:
                prevNode.next = kthnode

            prevNode = temp
            temp = nextNode

        return head              
