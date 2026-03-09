class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_str = str(x)[::-1]

        y = rev_str == str(x)
        return y
