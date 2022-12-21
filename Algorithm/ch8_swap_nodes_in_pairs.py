def swap(node):
    if not node or not node.next:
        return node
    else:
        node.val, node.next.val = node.next.val, node.val

        node.next.next = swap(node.next.next)

        return node


# 제출
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            head.val, head.next.val = head.next.val, head.val
            head.next.next = self.swapPairs(head.next.next)

            return head