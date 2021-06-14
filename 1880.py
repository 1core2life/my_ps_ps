class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        
        first = self.changer(firstWord)
        second = self.changer(secondWord)
        target = self.changer(targetWord)
        
        return (first + second == target)
    
    
    def changer(self, word):
        int_word_list = list()
        for wo in word:
            num = ord(wo) - 97
            int_word_list.append(num)
        
        result = 0
        idx = len(int_word_list) - 1
        for re in int_word_list:
            if re is not 0:
                result = result + re * 10**idx
            else:
                if idx is len(int_word_list) - 1:
                    pass
            idx = idx - 1
        
        return result
