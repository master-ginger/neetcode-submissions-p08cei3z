class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy=[]
        for i in range(len(nums)):
            copy.append([nums[i],i])
        copy.sort()
        l=0
        n=len(nums)
        r=n-1
        while l<r:
            curr=copy[l][0]+copy[r][0]
            if curr==target:
                    return [min(copy[l][1],copy[r][1]),max(copy[l][1],copy[r][1])]
            elif curr>target:
                r-=1
            else:
                l+=1
            

        