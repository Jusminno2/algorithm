from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        val = list(cnt.values())
        val.sort(reverse=True)
        top_k = val[:k]
        res = list()
        for l, m in cnt.items():
            if m in top_k:
                res.append(l)
        return res