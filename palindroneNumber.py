class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp = x
        while x>0:
            q=int(x/10)
            rem=x%10
            rev= rev * 10 + rem
            x=q
        return rev==temp