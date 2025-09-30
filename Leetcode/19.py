from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # n の間隔を持つポインタを2つ用意できれば、事は解決するな
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        # Null まで全力投球
        while right:
            right = right.next
            left = left.next

        # leftをleftの次の次のノードに結合
        left.next = left.next.next

        return dummy.next

