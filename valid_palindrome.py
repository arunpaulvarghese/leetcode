# program to find the palindrome of a sentense
class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l +=1
                r -=1
            else:
                return False
        return True

pal = 'malayalam'
sol = Solution()
print(sol.isPalindrome(pal))
