class Solution:
    def isPalindrome(self, s: str) -> bool:
        assert 1<=len(s)<=1000
        clean_str = "".join(char for char in s if char.isalnum())
        clean_lower_str=clean_str.lower()
        reverse_str=clean_lower_str[::-1]
        return clean_lower_str == reverse_str
