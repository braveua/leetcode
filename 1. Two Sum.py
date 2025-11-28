class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        for i,num in enumerate(nums):
            if target - num in nums[i + 1 :]:
                x=nums.index(target - num,i+1)
                return (i,x)
            

c = Solution()
res = c.twoSum([2,7,11,15],9)
print(res)