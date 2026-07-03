class Solution:
    def deleteNode(self, node: 'ListNode') -> None:
        # Copy the next node's value into this node
        node.val = node.next.val
        # Skip over the next node, effectively "deleting" it instead of node
        node.next = node.next.next
