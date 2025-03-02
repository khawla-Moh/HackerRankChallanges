class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] +nums[j] == target :
                    return [i ,j]

        return []        

            

o=Solution()
nums = [3,2,4]
target = 6
d=o.twoSum(nums,target)
print(d)

