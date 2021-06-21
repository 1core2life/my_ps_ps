class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split(' ')
        
        result = str('')
        for te in temp:
            length = len(te)
            result += "".join(str(te[length - idx - 1]) for idx in range(0, length))
            result += " "
        

        
        return result[:-1]
        
