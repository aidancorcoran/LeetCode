from solution import Solution, ListNode

headlinkedList1 = ListNode(1)
headlinkedList2 = ListNode(2)
headlinkedList3 = ListNode(4)

headlinkedList4 = ListNode(1)
headlinkedList5 = ListNode(3)
headlinkedList6 = ListNode(4)

headlinkedList1.next = headlinkedList2
headlinkedList2.next = headlinkedList3

headlinkedList4.next = headlinkedList5
headlinkedList5.next = headlinkedList6

solutionObj = Solution()

newList = solutionObj.mergeTwoLists(headlinkedList1, headlinkedList4)

while newList:
    print(newList.val)

    newList = newList.next
