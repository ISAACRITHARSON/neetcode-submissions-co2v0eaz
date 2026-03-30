class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #crating a hash map

        for i, n in enumerate(nums): #enumerating nums vale nad indedex
            diff = target - n #caculating differnce 
            if diff in prevMap:#condition if diff in hasmap
                return [prevMap[diff], i]#return 
            prevMap[n] = i
        return