class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        new_x=str(x)
        split_new_x = ''.join(new_x.split()).lower()
        return split_new_x==split_new_x[::-1]
            
        



solution=Solution()
result=solution.isPalindrome(10)
print(result)
