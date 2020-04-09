# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Answer:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)                  # head node
        node = head
        carry = 0                           # carry, default 0
        while l1 or l2:
            sum = 0
            if l1:
                sum = sum + l1.val
                l1 = l1.next                # update l1 node
            if l2:
                sum = sum + l2.val
                l2 = l2.next                # update l2 node
            node.next = ListNode((sum + carry) % 10)
            carry = (sum + carry) // 10               # carry for the next loop
            node = node.next                # update the node
        if carry > 0:       
            node.next = ListNode(1)         # if the last addition carry 1, need to add a node at the end of the list
        return head.next
