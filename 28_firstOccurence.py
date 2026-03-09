class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        m = len(haystack)
        if needle in haystack:
            for i in range(m-n+1):
                if haystack[i:i + n] == needle:
                    return i
        else:
            return -1
