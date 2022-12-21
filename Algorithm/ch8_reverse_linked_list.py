class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1, next=None))))


# 풀이 1

def reverse(node, prev = None):
    if not node:
        return prev

    next, node.next = node.next, prev

    return reverse(next, node)


print(reverse(head))


# 풀이 2 이게 메모리도 적게 쓰고 더 빠른다.

node = head
rev_node = None

while node:
    next, node.next = node.next, rev_node
    node, rev_node = next, node

print(rev_node)
