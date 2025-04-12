from __future__ import annotations
from typing import Any, Optional

from debugpy.common.timestamp import current


class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    def __init__(self, head:Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        """
        self.head.prev = new_node
        new_node.next = self.head
        
        を両方書く理由は双方向のつながりについて正しく記述するため
        => self.head.prev = new_node ⋯ new_node <- self.head(A) -> B -> *** -> None
        => new_node.next = self.head ⋯ new_node ⇄ self.head(A) -> B -> *** -> None
        => self.head = new_node ⋯ self.head(new_node) ⇄ A -> B -> *** -> None
        """
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        current_node = self.head
        # 先頭のdataを削除する場合
        if current_node and current_node.data == data:
            # head -> a -> None の場合
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            # head -> a -> b -> *** -> None の場合
            else:
                next_node = current_node.next
                current_node = None
                next_node.prev = None
                self.head = next_node
                return

        while current_node and current_node.data != data:
            current_node = current_node.next

        # 該当の数値がなかった場合：
        if current_node is None:
            return

        # 該当の数値があり、その数値が最後尾にあった場合...
        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return
        # 該当の数値が存在し、かつ該当の数値がリストの橋ではない場合...
        else:
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head

        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next   # ここがミソ=>prevを呼び出す必要がある！
            current_node.next = previous_node
            current_node = current_node.prev    # current_nodeの更新を忘れてはいけない

        if previous_node:
            self.head = previous_node.prev

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node) -> Optional[Node]:
            if not current_node:
                return None

            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node

            if current_node.prev is None:
                return current_node

            # ここがミソ！ => current_node.prev
            # もしここに current_nodeを引数として入れたら無限ループになる
            return _reverse_recursive(current_node.prev)

        self.head = _reverse_recursive(self.head)

    # bubbleソートでやってみる
    def sort(self) -> None:
        if self.head is None:
            return

        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next

            current_node = current_node.next

    # def sort_original(self) -> None:
    #     if self.head is None:
    #         return
    #     current_node = self.head
    #     while current_node.next:
    #         while current_node.next:
    #             next_node = current_node.next
    #             if current_node.data > current_node.next.data:
    #                 current_node.next.data = current_node.data
    #                 current_node.data = next_node.data
    #             next_node = next_node.next
    #         current_node = current_node.next








if __name__ == '__main__':
    d = DoublyLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    d.insert(0)
    # d.remove(2)
    d.print()
    print("######## ReverseIterate #######")
    d.reverse_iterative()
    d.print()
    # print("######## ReverseRecursive #######")
    # d.reverse_recursive()
    # d.print()
    print("######## sort #######")
    d.sort_original()
    d.print()

