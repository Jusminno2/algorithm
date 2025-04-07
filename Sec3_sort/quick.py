from typing import List

"""
partition_funcの役割
・配列内の並びをじゃんじゃん変更していく
・forループが終了したら、pivotをi+1番目の数字と入れ替える
・i+1をindexとしてreturnする
"""
def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i + 1


"""
quick_sortの役割
・partition_funcを呼び出して配列のソートしていく
・再帰関数として、low<highの限りに処理は続行する

なぜ関数内関数を使用したのか？
・特に外部で関数を出しておく必要性がないから

quick_sort理解のために...
・numbersを渡してhighとlow別々に処理をしているが、順番としては、low=>highとなっている
・low=highになるとき=>一つしか数字がなくなったとき
"""
def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) ->  None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index - 1)
            _quick_sort(numbers, partition_index + 1, high)

    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers


if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    print(quick_sort(nums))