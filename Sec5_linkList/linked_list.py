from __future__ import annotations
from typing import Any


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


if __name__ == "__main__":
    # まず、インスタンスを生成してから内部の関数を使用
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert(0)
    ll.print()
    ll.remove(2)
    print("################")
    ll.print()
    # print(ll.head.data) # 中身の数値を指す
    # print(ll.head.next) # 次のノードオブジェクトを指す
    # print(ll.head.next.data)
    # print(ll.head.next.next.data)
    # print(ll.head.next.next.next.data)