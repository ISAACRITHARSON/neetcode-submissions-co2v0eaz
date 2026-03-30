class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialising empty string
        newstr=''
        for c in s:
            #isalnum is alpha
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]