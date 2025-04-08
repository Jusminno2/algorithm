from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    """
    :param numbers:

    役割：
    ・Nlog(N) の計算量
    ・安定ソート
    ・numbersを分割していく
    ・再帰的に呼び出しを行い、左と右に分けて処理を進めていく
    ・今回であれば...
                        8
                       4 4
                     2 2 2 2 　　　
                 1 1 1 1 1 1 1 1   <= これ以上分割できなくなる
                     2 2 2 2       <= それぞれをnumbersとしてwhileで処理する
                       4 4
                        8
    """
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    """
    ここからは、numbersについてsortしていく
    :param 
    i: 左側のインデックスを表す
    j: 右側のインデックスを表す
    k: numbersに格納するためパラメータ
    """
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


if __name__ == '__main__':
    numbers = [5, 4, 1, 8, 7, 3, 2, 9]
    print(merge_sort(numbers))