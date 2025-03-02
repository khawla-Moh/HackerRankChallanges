# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        convert_ls1=int(''.join(str(num) for num in l1) )
        convert_l2=int(''.join(str(num) for num in l2) )
        sum_numbers=convert_ls1+convert_l2    
        
        return[int(num) for  num in str(sum_numbers)][::-1]


o=Solution()
l1=[2,4,3]
l2 = [5,6,4]
d=o.addTwoNumbers(l1,l2)
print(d)


""" 
l=[9,9,9,9,9,9,9]
l2=[9,9,9,9]
print(l)
print(l2)
print('####**###')
[8,9,9,9,0,0,0,1]
ls0=int(''.join(str(num) for num in l) )
ls1=int(''.join(str(num) for num in l2) )
print(ls0)    
print(ls1)
sum0=ls0+ls1    
print(sum0)
print([int(num) for  num in str(sum0)][::-1])
 """



