from __future__ import annotations
from typing import Any, Optional

"""
「-> None」 の意味：この関数には戻り値がありませんよ！という意味

クラスを使用する意味：
・データ（状態）と処理（動作）をひとまとまりにできる
    => head をグローバルに持ち出す必要がある
    => そのデータが何（引数｜関数）を持っていて、どう動くのかをひとつにまとめて表現できる
・関連する処理を整理して、使いやすくできる
・複数のリスト（インスタンス）を独立して扱える
    => 何個でもリンクリストを作れるし、それぞれ独立して動作
・再利用性、拡張性が高くなる
"""
class Node(object):
    def __init__(self, data: Any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    """
    概念の考え方：=を→で考えるとわかりやすい
    ・data|nextのnext部分は次のノードの情報が入っていると考える
    ・self.head = new_node ⋯⋯ head->new_node で並んでいますよ
    ・last_node.next = new_node ⋯⋯ head->node1->node2->node3->last_node->new_node で並んでいますよ
    """
    def append(self, data: Any) -> None:
        new_node = Node(data)
        """
        if文でreturnを記述する理由：
        ・早く操作を抜けたい=>必要のない処理が後述に続く場合に有効
        """
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    # 先頭にノードを挿入
    """
    returnを用いない理由：
    ・なにかの値を返す必要がない
    ・内部で操作だけをして完結している
    """
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head  # new_node->head->node1->node2->***->last_node->None
        self.head = new_node       # head->new_node->node1->node2->***->last_node->None

    # 繰り返しprint文を記述するのが助長なためprint文を新たに定義
    def print(self) -> None:
        current_node = self.head
        # 最後尾のNoneにぶち当たるまで実行
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        """
        見つかった最初の数字だけを削除=>同じ数字が複数ある場合は、一つしか削除できない
        """
        current_node = self.head
        if current_node and current_node.data == data: # head->want_to_remove->node1->***->last_node->None
            self.head = current_node.next              # head->node1->***->last_node->None
            current_node = None
            return
        """
        なぜ previous_node を定義する？
        => head 代わりにするため｜移動するheadと考える
        => previous_node->current_node(want_to_remove)->node1 を...
        => previous_node->node1 という順に変更したい！
        """
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = previous_node.next

        # current_node.data == data が見つからずに最後尾のNoneに到達した場合
        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node.next = None

    def reverse_iterative(self) -> None:
        """
        head->node1->node2->***->last_node->None
                    ↓ reverse ↓
        head<-node1<-node2<-***<-last_node<-None

        概念：
        ・previous_node <- current_node をずらしていくイメージ
        ・はじめは、None <- previous_node <- current_node <- ***

        変数：
        ・previous_node|current_node|next_node という位置関係を保持したまま、
        　while で右にずらしていく
        ・結局やりたいのは、previous_node<-current_node(current_node.next=previous_node)である
        """
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    """
    頻出問題
    
    再帰タイプ：前から進んで処理を行うタイプ
    """
    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node) -> Node:
            if not current_node:
                return previous_node

            next_node = current_node.next       # 次のノードを一旦退避=>矢印の向きが変化するので右側に渡れる島を作っておく
            current_node.next = previous_node   # ここがミソ！
            previous_node = current_node        # previous 右ずらし
            current_node = next_node            # current 右ずらし
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)

    """
    練習問題：偶数が続いているときだけ逆方向にしろ
    """
    def reverse_even(self) -> None:
        """
        偶数が連続する場合のみ、順番をリバースさせる
        例1：1, 4, 6, 8, 9 => 1, 8, 6, 4, 9
        例2：1, 4, 6, 8, 9, 1, 4, 6, 8, 9 => 1, 8, 6, 4, 9, 1, 8, 6, 4, 9
        例3：1, 3, 5 => 1, 3, 5
        """
        def _reverse_even(head: Node, previous_node: Node) -> Optional[Node]:
            if head is None:
                return None

            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
                return head

        # この部分で渡しているself.headはappend関数で先頭の数字であると定義済み
        self.head = _reverse_even(self.head, None)


if __name__ == "__main__":
    # まず、インスタンスを生成してから内部の関数を使用
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    # ll.insert(0)
    ll.print()
    # ll.remove(2)
    print("################")
    ll.reverse_iterative()
    ll.print()
    print("###############")
    ll.reverse_recursive()
    ll.print()
    # print(ll.head.data) # 中身の数値を指す
    # print(ll.head.next) # 次のノードオブジェクトを指す
    # print(ll.head.next.data)
    # print(ll.head.next.next.data)
    # print(ll.head.next.next.next.data)