from typing import List

"""
Selection（選択）ソートは、配列から最小（または最大）の要素を「選んで」、
それを先頭に「交換」していく、シンプルなソートアルゴリズム
"""
def selection_sort(arr: list[int]) -> list[int]:
    len_numbers = len(arr)
    for i in range(len_numbers):
        min_index = i
        for j in range(i+1, len_numbers):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    import random
    arr = [random.randint(0, 10000) for i in range(10)]
    print(selection_sort(arr))