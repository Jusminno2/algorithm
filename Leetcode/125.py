class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and self.isalnum(s[l]) != True:
                l += 1
            while l < r and self.isalnum(s[r]) != True:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isalnum(self, c: str) -> bool:
        return (
                ord('0') <= ord(c) <= ord('9') or
                ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z')
        )