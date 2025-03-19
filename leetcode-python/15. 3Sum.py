class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """
        if nums is None or len(nums) ==1:
            return None
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            left,right=i+1,len(nums)-1
            while left < right:
                total =nums[i]+nums[left]+nums[right]
                if total ==0:
                    res.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                elif total >0:
                    right -=1
                else:
                    left +=1
        return res        
