# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        head = list1
        for i in range(a - 1):
            head = head.next

        tail = list1
        for i in range(b + 1):
            tail = tail.next

        head.next = list2
        while head.next:
            head = head.next

        head.next = tail

        return list1
