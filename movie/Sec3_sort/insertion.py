from typing import List


"""
特徴
・for文が1からスタート -> 左にずらしていくため
・tempは常に固定で、左にtempより大きいものがある場合に処理続行
・whileに入る限りは、j番目の値をj+1番目にスライドしていく->右に値をずらしていく
"""
def insertion__sort(arr: List[int]) -> List[int]:
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]
        j = i -1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

    return arr


if __name__ == "__main__":
    import random
    arr = [random.randint(1, 1000) for _ in range(10)]
    print(insertion__sort(arr))

