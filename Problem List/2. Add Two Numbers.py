# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        current = result
        current1 = l1
        current2 = l2
        pre = 0
        while current1 is not None and current2 is not None:
            tmp = current1.val + current2.val + pre
            val = tmp % 10
            new_node = ListNode(val)
            while current.next:
                current = current.next
            current.next = new_node

            if tmp >= 10:
                pre = 1
            else:
                pre = 0
            current1 = current1.next
            current2 = current2.next
        while current1 is not None:
            tmp = current1.val + pre
            val = tmp % 10
            new_node = ListNode(val)
            while current.next:
                current = current.next
            current.next = new_node

            if tmp >= 10:
                pre = 1
            else:
                pre = 0
            current1 = current1.next
        while current2 is not None:
            tmp = current2.val + pre
            val = tmp % 10
            new_node = ListNode(val)
            while current.next:
                current = current.next
            current.next = new_node

            if tmp >= 10:
                pre = 1
            else:
                pre = 0
            current2 = current2.next
        if pre is not 0:
            new_node = ListNode(pre)
            while current.next:
                current = current.next
            current.next = new_node
        return result.next
            

        