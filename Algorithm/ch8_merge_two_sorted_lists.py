# l1, l2는 연결리스트

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))

def mergeTwoLists(list1, list2):
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1

    if list1:
        list1.next = mergeTwoLists(list1.next, list2)

    return list1

print(mergeTwoLists(list1, list2))