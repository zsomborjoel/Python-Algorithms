"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

For example, 12321 is palindrome, but 1451 is not palindrome. 
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        pre_list = list(str(x))
        new_list = []

        for i in reversed(pre_list):
            new_list.append(i)

        if pre_list == new_list:
            return True
        else:
            return False
