"""
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[8, 9] => [9, 0] => 90
[9, 9] => [1, 0, 0] => 100
[1, 2, 3] => [1, 2, 4] => 124
[7, 8, 9] => [7, 9, 0] => 790
[9, 9, 9] => [1, 0, 0, 0] => 1000
[0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
"""
from typing import List

def list_to_int(numbers: List[int]) -> int:
    """
    num = 0
    length = len(numbers)
    for i in range(length):
        num += numbers[i] * 10 ** [length - i - 1]
    return num
    """
    sum_numbers = 0
    for index, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10**index)
    return sum_numbers


def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        return remove_zero(numbers)


def plus_list(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        # 7, 8, 9 => 7, 9, 10
        # 8, 9, 9 => i=2 => 8, 9, 10 => 8, 10, 0 => i=1 => 9, 0, 0 => OK!!!
        # 9, 9, 9 => i=2 => 9, 9, 10 => 9, 10, 0 => i=1 => 10, 0, 0 => else => 1, 0, 0, 0（最後にappend）
        numbers[i] = 0
        numbers[i - 1] += 1
        i -= 1
    # while-else文はbreakが実行されない場合（while文がすべて実行された場合にelseの処理を実行するというもの
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)


if __name__ == '__main__':
    print(plus_list([0, 0, 0, 9, 9, 9, 9]))





