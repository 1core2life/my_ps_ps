class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        str_num = list(str(num))
        for nu in str_num:
            if nu is '6':
                str_num[str_num.index(nu)] = '9'
                break
        
        return "".join(str_num)
            
