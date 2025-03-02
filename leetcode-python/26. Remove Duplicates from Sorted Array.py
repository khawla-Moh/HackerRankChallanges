class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_num=0
        for i in range(1,len(nums)):
            if nums[i] != nums[unique_num]:
                unique_num += 1
                nums[unique_num] = nums[i]

        return unique_num +1        

        
        
        
        
        """ 
        l=[]
        s=[i for i in nums if  not (i in l  or l.append(i) ) ]
        return s
         """ 
        #return len(list(set(nums)))
                


o=Solution()
d=o.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(d)