# 이해하기 어렵지만 계속 참조를 반복해나가는 것이다.
# even_head는 2, 3, 4, 5를 가지고 있으면서 even을 바꿀 때마다 참조로 인해서 2, 4, 5 -> 2, 4로 바뀐다.
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head
