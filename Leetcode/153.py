from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]
        while l <= r:
            mid_idx = l + (r-l)//2
            if nums[mid_idx] < res:
                res = min(res, nums[mid_idx])
                r = mid_idx - 1
            else:
                l = mid_idx + 1
        return res