from typing import List, NewType

IndexNum = NewType("IndexNum", int)


def linear_search(numbers: List[int], value: int) -> IndexNum:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


# def binary_search(numbers: List[int], value: int) -> IndexNum:
#     """
#     前提：数字がソートされた後であること
#
#     以下をleft<=right（追い越さない）限り続ける
#     ・middleよりもその数値が左側であれば...rightをずらす
#     ・middleよりもその数値が右側であれば...leftをずらす
#     """
#     left, right = 0, len(numbers) -1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


"""
なぜ、インナー関数を用いるのか？
=> 内部ロジックを隠蔽するため（カプセル化）⋯ 再帰処理用の補助関数であり、外部から呼び出したくないから
=> 初期値のパラメータが多くなると利用がめんどくさい ⋯ いちいち書く必要がある
"""

# 再帰で書けと言われた場合...
def binary_search(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], value: int, left: IndexNum, right: IndexNum) -> IndexNum:
        """
        以下のように定義する必要がない
        left, right = 0, len(numbers) - 1
        """

        # left <= right の逆
        if left > right:
            return -1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] > value:
            return _binary_search(numbers, value, left, mid - 1)
        else:
            return _binary_search(numbers, value, mid + 1, right)

    # ここのreturnは外部関数に関するもの
    return _binary_search(numbers, value, 0, len(numbers) - 1)


if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 23]
    # print(linear_search(numbers, 5))
    print(binary_search(nums, 15))