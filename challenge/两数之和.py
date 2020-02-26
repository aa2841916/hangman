

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for n in range(0,len(nums)):
        #     for num in range(0,len(nums)):
        #         if nums[n] + nums[num] == target and nums[n] != nums[num] and n < num:
        #             return [n,num]
        #         elif nums[n] + nums[num] == target and n == num:
        #             continue
        #         elif nums[n] == nums[num] and nums[n] + nums[num] == target and n > num:
        #             return [num,n]

        a = {}
        for i,j in enumerate(nums):
            if j in a:
                return [a.get(j),i]
            a[target - j] = i


if __name__ == '__main__':
    x = [3,2,4]
    y = 6
    so = Solution()
    ty = so.twoSum(x,y)
