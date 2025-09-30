from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 連結リストの中央を探す
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 右側の連結リストをリバースする
        # 右連結先頭へのポインタの移動
        second = slow.next
        # 左連結と右連結を完全に切り離す
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 左->右->左->右->左->右->⋯
        first, second = head, prev
        # 【重要】連結切れる前に保存しとけ,secondが先終わるか一緒
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



