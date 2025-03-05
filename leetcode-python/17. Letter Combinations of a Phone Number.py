




class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        digit_representations={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','v','u'],
            '9':['w','x','y','z'],
        }
        while  True:
            if not digits:
                return []
            if digits[0]=='1':
                return []
    
            if len(digits)==1:
                return digit_representations[digits]
            elif len(digits)>=2:
                return [a+b for a in digit_representations[digits[0]] for b in self.letterCombinations(digits[1:])]  

        return
        
