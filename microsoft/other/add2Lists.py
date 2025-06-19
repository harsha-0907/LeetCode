
class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None

class Solution:
    def add2Lists(head1, head2):
        carry = 0; newHead = parent = Node()
        while head1 or head2:
            h1 = head1.val if head1 else 0
            h2 = head2.val if head2 else 0
            n, carry = (h1+h2+carry)%10, (h1+h2+carry)//10
            newNode = Node(n)
            parent.next = newNode
            parent = parent.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        if carry > 0:
            newNode = Node(carry)
            parent.next = newNode

        return newHead.next
