class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num_str = ""
        out_list = []
        for i in digits:
            num_str += str(i)

        out_str = str(int(num_str)+1)

        for i in out_str:
            out_list.append(int(i))

        return out_list
