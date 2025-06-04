from typing import List


"""
O(N^2)の回答

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for id_i, num_i in enumerate(nums):
            for id_j, num_j in enumerate(nums):
                if id_i == id_j:
                    continue
                else:
                    if num_i + num_j == target:
                        return [id_i, id_j]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = list()
        for num in nums:
            rest = target - num
            if rest > 0:
                cache.append(num)
