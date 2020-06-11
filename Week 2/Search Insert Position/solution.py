class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums)
        while first < last:
            mid = (first+last)//2
            if nums[mid] >= target:
                last = mid
            else:
                first = mid + 1
        return first

nums = [1,3,5,6]
target = 5
obj = Solution()
print(obj.searchInsert(nums, target))