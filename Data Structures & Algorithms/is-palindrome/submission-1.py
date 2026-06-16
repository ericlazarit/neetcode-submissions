class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        reversed = s[::-1]
        return (s == reversed)