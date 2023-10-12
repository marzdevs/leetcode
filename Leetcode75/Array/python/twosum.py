class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for key, value in enumerate(nums):
            vals = target - value 

            if vals in found:
                return [found[vals], key]

            found[value] = key
