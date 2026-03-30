class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dic 
        count = {}
        #create a for loop to find the frequentcy of elemt in the top k
        for num in nums:
            count[num]= 1 + count.get(num,0)

        #create an empty array to append count, number
        arr=[]
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        #creating a list so to pop large count and append in array
        res =[]
        #while loop for less than k condition check
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
