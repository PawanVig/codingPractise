class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        length = len(nums)
        for i in range(length):
            delta = target - nums[i]
            if delta in dic.keys():
                return {dic[delta], i}
            dic[nums[i]] = i
        return null