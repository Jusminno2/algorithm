import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict(collections.Counter(s))
        t_dict = dict(collections.Counter(t))

        if s_dict == t_dict:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    s = "racecar"
    t = "carrace"
    result = solution.isAnagram(s, t)
    print(result)