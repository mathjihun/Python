# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next     # 연결 리스트의 정의에 따라 다음 요소를 갖고 있는 것이다.
    def __str__(self):
        return f'val: {self.val}, next: {self.next}'
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1, next=None))))

reverse_head = ListNode(head.val, next=None)
cur_node = head

while cur_node.next != None:
    cur_node = cur_node.next
    reverse_head = ListNode(val=cur_node.val, next=reverse_head)


print(head)
print(reverse_head)
print(reverse_head == head)    # 이런걸 처리하려면 따로 class에 정의가 필요

print()

q = []

if not head:
    print(True)

node = head

while node is not None:
    q.append(node.val)
    node = node.next

if q == list(reversed(q)):
    print(True)
else:
    print(False)

print()

# 책 deque 활용

import collections

q = collections.deque()

if not head:
    print(True)

node = head

while node is not None:
    q.append(node.val)
    node = node.next

while len(q) > 1:
    if q.popleft() != q.pop():
        print(False)

print(True)


# 책 runner 기법 활용

rev = None
slow = fast = head

while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next

if fast:
    slow = slow.next

while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next

return not rev