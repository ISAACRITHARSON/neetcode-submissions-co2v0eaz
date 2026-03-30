class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result=0
        numbers = set(nums)
        for num in numbers:
            streak, curr = 0, num
            while curr in numbers:
                streak +=1
                curr +=1 
            result = max (result, streak)
        return result

        