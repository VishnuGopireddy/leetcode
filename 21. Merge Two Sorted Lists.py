# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = l1
        list2 = l2
        list3 = None
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr = curr1
                curr1 = curr1.next
            else:
                curr = curr2
                curr2 = curr2.next

            curr.next = None
            if list3 == None:
                list3 = curr
            else:
                temp = list3
                while temp.next != None:
                    temp = temp.next
                temp.next = curr

        if curr1:
            curr = curr1
            if list3 == None:
                list3 = curr
            else:
                temp = list3
                while temp.next != None:
                    temp = temp.next
                temp.next = curr

        if curr2:
            curr = curr2
            if list3 == None:
                list3 = curr
            else:
                temp = list3
                while temp.next != None:
                    temp = temp.next
                temp.next = curr

        return list3