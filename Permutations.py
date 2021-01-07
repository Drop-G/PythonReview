class Solution(object):
    def _permuteHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]
        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            result += self._permuteHelper(nums, start+1)
            nums[start], nums[i] = nums[i], nums[start]
        return result
    def permute(self, nums):
        return self._permuteHelper(nums)


print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
