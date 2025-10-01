from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 元のコピーを参照したい→HashMapで表現可能
        oldToCopy = {None: None}

        # HashMapにポインタを持たないコピーノードを登録
        # cur ではもとの連結リストを指す
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # もとのHashMapを参照しながらポインタを追加していく
        # このループが終わるとポインタ付きのHashMapに変更される
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        # ポインタ付きのHashMapの先頭を返せば終わり
        return oldToCopy[head]