from __future__ import annotations
from typing import Any

class Node(object):
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node


class LinkList(object):
    def __init__(self, head: Node = None):
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        # last node を右にずらす
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        '''
        やることは2つ
        1. これまでの head を next node にする
        2. new node を next node にする
        '''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data: Any) -> None:
        current = self.head
        # 先頭の場合
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        # 先頭ではない場合
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        # なにもデータに該当しなかった場合
        if current is None:
            return

        previous.next = current.next
        current = None



if __name__ == '__main__':
    link_list = LinkList()
    link_list.append(1)
    link_list.append(2)
    link_list.append(3)
    link_list.insert(0)
    print(link_list.head.data)
    print(link_list.head.next.data)
    print(link_list.head.next.next.data)
    link_list.remove(2)
    print(link_list.head.data)
    print(link_list.head.next.data)
    print(link_list.head.next.next.data)