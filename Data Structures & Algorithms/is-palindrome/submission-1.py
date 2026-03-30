class Solution:
    def isPalindrome(self, s: str) -> bool: 
        clean =""
        for i in range (len(s)):
            if s[i].isalnum():
               clean+=s[i].lower()
        return clean == clean[::-1]



