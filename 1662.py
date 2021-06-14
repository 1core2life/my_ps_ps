class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
                
        f_word = str()
        for word in word1:
            f_word += word
        
        s_word = str()
        for word in word2:
            s_word += word
        
        return f_word == s_word
