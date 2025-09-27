from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rest_num = list()
        for i in range(len(numbers)):
            current = numbers[i]
            if current in rest_num:
                index1 = rest_num.index(current) + 1
                index2 = i + 1
                return ([index1, index2])

            else:
                rest = target - numbers[i]
                rest_num.append(rest)