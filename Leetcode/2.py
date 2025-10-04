from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 新規のLinkedList作成と言ったら、dummyの出番
        dummy = ListNode()
        current = dummy

        # 繰り上げというエッジケースを考慮
        curryUp = 0

        while l1 or l2 or curryUp:
            # Noneであっても0という意味はもつからね
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2

            # 繰り上げを考慮していく
            carryUp = val // 10
            # 15 -> 10(carryUp) + 5(val)
            val = val % 10
            current.next = ListNode(val)

            # pointer の更新
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
