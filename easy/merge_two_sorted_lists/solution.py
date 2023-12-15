# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        mergedList = [ListNode]
        headPtr = mergedList

        list1_ptr = list1
        list2_ptr = list2
        while list1_ptr.next != None and list2_ptr.next != None:
            if list1_ptr.val == list2_ptr.val:
                mergedList.append(list1_ptr)
                mergedList.append(list2_ptr)

                list1_ptr = list1_ptr.next
                list2_ptr = list2_ptr.next
            elif list1_ptr.val < list2_ptr.val:
                mergedList.append(list1_ptr)

                list1_ptr = list1_ptr.next
            else:
                mergedList.append(list2_ptr)

                list2_ptr = list2_ptr.next

        return headPtr