from solution import Solution, ListNode

def printLinkedList(list_head):
    item_cur = list_head
    while item_cur != None:
        print(item_cur.val)
        item_cur = item_cur.next

solutionObj = Solution()

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node1.next = node2 
node2.next = node3
node3.next = node4
node4.next = node5

printLinkedList(node1)








