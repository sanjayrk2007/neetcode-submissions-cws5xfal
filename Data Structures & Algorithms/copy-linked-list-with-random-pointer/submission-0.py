"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        o={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            o[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=o[cur]
            copy.next=o[cur.next]
            copy.random = o[cur.random]
            cur=cur.next
        return o[head]