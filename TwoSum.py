# What are the two unique numbers

class Solution(object):
    def twoSum(self, nums, target):
        for i1, a in enumerate(nums):
            for i2 , b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return [i1, i2]
        return []

    def twoSumB(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in values:
                return [i, values[difference]]
            values[num] = i
        return []

    
print (Solution().twoSum([2,7,11,15], 18))