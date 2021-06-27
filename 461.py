class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        x = bin(x)[2:]
        y = bin(y)[2:]


        selected = 0
        if len(x) > len(y):
            selected = len(x)
            for idx in range(0, selected - len(y)):
                y = '0' + y
        else:
            selected = len(y)
            for idx in range(0, selected - len(x)):
                x = '0' + x

        result = 0
        for idx in range(0, selected):
            if x[idx] != y[idx]:
                result += 1
        
        return result
