from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # もし配列のサイズが1の場合でも対応できるようにイコールをつける
        while l <= r:
            m = l + (r - l) // 2
            # もし、正解出たらここでリターン
            if target == nums[m]:
                return m

            # もし中央の値が左側グループに属する場合...
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            # もし中央の値が右側のグループに属する場合...
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1