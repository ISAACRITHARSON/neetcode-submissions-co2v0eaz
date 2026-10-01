#you take each number for nums and compare it witth the set seen if the number is alrady available return true else we add the nber to set seen and return false
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False        
        


