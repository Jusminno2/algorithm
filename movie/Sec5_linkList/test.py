from __future__ import annotations
from typing import Any

class Node(object):
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        self.head = new_node
        new_node.next = last_node

    def remove(self, data: Any) -> None:
        current_node = self.head

        # 先頭との場合分けができるか否か => 削除対象が head の場合、previous_node が存在しない（previous_node が None なので AttributeError になる）
        if current_node and current_node.data == data:
            self.head = current_node.next
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next

    def reverse_iterative(self) -> None:
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            # 明確に違う => 初期段階ですでに current_node を None にできる
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node):
            if current_node is None:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)






if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(4)
    l.insert(5)
    l.remove(5)
    print(l.head.data)
    print(l.head.next.data)
    print(l.head.next.next.data)
    print(l.head.next.next.next.data)
    l.reverse_recursive()
    print('#######################################')
    print(l.head.data)
    print(l.head.next.data)
    print(l.head.next.next.data)
    print(l.head.next.next.next.data)