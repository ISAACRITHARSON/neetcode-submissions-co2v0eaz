class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l,r = 0, len(numbers) - 1 
            while l<r:
                Sum = numbers[l] +numbers[r]
                if Sum> target:
                    r= r-1
                elif Sum< target:
                    l=l+1
                else:
                    return [l+1, r+1]
            return[]


        