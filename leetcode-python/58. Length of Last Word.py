class Solution(object):
    def lengthOfLastWord(self, s):
        new_string=s.rstrip()
        return len([i for i in new_string.split(' ') ][-1])
              
                   
         
         


o=Solution()
s="   fly me   to   the moon  "

d=o.lengthOfLastWord(s)
print(d)        