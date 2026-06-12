#PALINDROME NUMBER 
class Solution(object):
    def isPalindrome(x):
        temp=x
        rev=0
        i=len(str(x))
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        return rev==temp
    
print(Solution.isPalindrome(121))
print(Solution.isPalindrome(-121))
print(Solution.isPalindrome(10))

#VALID PALINDROME FOR STRING
class Solution(object):
    def isPalindrome(s):
        import re
        temp=s.lower().strip()
        rev=(s[::-1]).lower().strip()
        return re.sub(r'[^a-zA-Z0-9]','',rev)==re.sub(r'[^a-zA-Z0-9]','', temp)

print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
print(Solution.isPalindrome("race a car"))
print(Solution.isPalindrome(" "))
        