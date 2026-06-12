class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = self.lowerCleaned(s)
        return clean == clean[::-1]

    def lowerCleaned(self, s):
        cleaned = ''

        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        return cleaned