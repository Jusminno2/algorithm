from executing.executing import node_linenos
from mistune.plugins.formatting import insert


class Node(object):

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self) -> None:
        # インスタンスを生成した時点ではroot=None
        self.root = None

    def insert(self, value: int) -> None:
        # insert を値を追加する操作であるから、Nodeがもともとない場合は作成してそのまま返すだけ
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            # この部分はnodeが子ノードにない場合でま新しく作る必要があるので大事
            # None になるかどうかを判定するこの部分が最重要かも
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)


    def inorder(self) -> None:
        def _inorder(node:Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)

        _inorder(self.root)


    def search(self, value: int) -> bool:
        def _search(node:Node, value: int) -> bool:
            if node is None:
                return False

            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)

        return _search(self.root, value)


    def min_value(self, node:Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ここは難しそう
    def remove(self, value: int) -> None:
        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return node

            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        _remove(self.root, value)



if __name__ == '__main__':
    """
    root とはそこを起点とした木構造全体を表す
    """
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    binary_tree.inorder()
    print(binary_tree.search(6))
    binary_tree.remove(6)
    print("###### Remove#######")
    binary_tree.inorder()

    """
    クラスを用いない場合の出力：
    
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)

    print(search(root, 2))
    print(inorder(root))
    print(root)
    print(root.left.right.value)
    """
