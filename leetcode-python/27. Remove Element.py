class Solution(object):

    def removeElement(self, nums, val):
        s=[]
        value=0
        for index,num in enumerate(nums):
            if index == val:
                value=num
                if value == val:
                    s.append(num)

                


                
                
                
        print(s)
        return len(s)        
            

o=Solution()

d=o.removeElement([2,2,3,3],3)        
print(d)
    
    #not correct answer
""" def removeElement(self, nums, val):

        # Find the positions of the number
        value=0        
        for index,num in enumerate(nums):
                if index==val:
                     value=num
        update_nums=[_ if num == value else num for num in nums]  

        numbers = [item for item in update_nums if item != '_']
        underscores = ['_' for item in update_nums if item == '_']

        # Combine the results
        ordered = numbers + underscores

        return ordered 
 """

    #not correct answer
"""
    def rmoveElemnt2(self,nums,val):
       
        # Pointer for the position to write the next valid element
        value = 0
        
        # Iterate through the list with index and value
        for index, num in enumerate(nums):
            if num != val:
                # Assign the valid element to the position indicated by value
                nums[value] = num
                value += 1  # Move to the next position
                
        return value  # Return the new length
"""

