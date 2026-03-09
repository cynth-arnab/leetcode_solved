class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        len1 = len(word1)
        len2 = len(word2)

        minlen = min(len1,len2)

        for i in range(0,minlen):
            merged += word1[i] + word2[i]

        if len1>len2:
            for i in range(minlen,len1):
                merged+=word1[i]

        if len1<len2:
            for i in range(minlen,len2):
                merged+=word2[i]

        return merged
