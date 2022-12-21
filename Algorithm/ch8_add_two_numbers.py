# 내 풀이 속도는 괜찮으나 메모리를 많이 사용한다. 비교해보면 책들보다도 빠름

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(l1, l2, count=0):
    if (not l1) and (not l2):
        if count == 1:
            return ListNode(val=1, next=None)
        else:
            return None

    else:
        if not l1:
            l1 = ListNode(val=0)
        if not l2:
            l2 = ListNode(val=0)

        if l1.val + l2.val + count >= 10:
            return ListNode(val=l1.val + l2.val - 10 + count, next=add(l1.next, l2.next, 1))
        else:
            return ListNode(val=l1.val + l2.val + count, next=add(l1.next, l2.next, 0))


l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None))))
l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))))))

print(add(l1, l2, 0))


#책 메모리 더 적게 사용한다 단, 몇 번 해보니 속도는 평균적으로 좀 더 느린듯 그런데 큰 차이는 없다.
# 메모리는 count 때문인 듯 하다.

root = head = ListNode(0)

carry = 0
while l1 or l2 or carry:
    sum = 0

    if l1:
        sum += l1.val
        l1 = l1.next
    if l2:
        sum += l2.val
        l2 = l2.next

    carry, val = divmod(sum + carry, 10)
    head.next = ListNode(val)
    head = head.next

return root.next