class Solution:
    def twoSum(self, nums, target):
        #"""
        #:type nums: List[int]
        #:type target: int
        #:rtype: List[int]
        #"""     
        for i in range(len(nums)):
            d = target - nums[i]
            if d in nums:
                j = nums.index(d)
                if i!=j:  #judge whether i is equal to j
                    if i<j : #decide the order of output
                        return [i, j]
                    else:
                        return [j,i]
