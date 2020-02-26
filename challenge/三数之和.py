class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        nums_dict = []
        nums.sort()
        if len(nums) < 3:
            return []
        elif len(nums) == 3 and nums.count(0) == 2:
            return []
        elif len(nums) == nums.count(0):
            return [[0, 0, 0]]

        for i in nums:
            for j in nums:
                if i == j:
                    continue
                elif -(i + j) in nums:
                    nums_dict.append([i,j,-(i + j)])
                    if i == j:
                        nums.remove(i)
                        if i in nums:
                            nums.remove(-(i + j))
                    else:
                        nums.remove(j)
                        nums.remove(-(i + j))

        # nums_dict.pop(0)



        # for c in nums_dict:
        #     nums_dict.pop(0)
        #     if c in nums_dict:
        #         nums_dict_2.append(c)




        print(nums_dict)





if __name__ == '__main__':
    tee = Solution()
    tyy = tee.threeSum([-1, 0, 1, 2, -1, -4,3])




