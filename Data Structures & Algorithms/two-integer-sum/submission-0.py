class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res  = []
        dict1 = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in dict1:
                dict1[nums[i]] = i
            else:
                if i < dict1[target - nums[i]]:
                    res = [i, dict1[target - nums[i]]]
                else:
                    res = [dict1[target - nums[i]], i]
        return res