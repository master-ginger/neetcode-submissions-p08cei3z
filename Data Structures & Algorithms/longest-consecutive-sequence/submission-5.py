class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        max_len=0
        num_set = set(nums)
        if len(list(set(nums)))==1:
            return 1
        for num in num_set:
            
            if num+1 in num_set:
                length=1
                curr=num
                while curr+1 in num_set:
                    length+=1
                    curr+=1
                max_len=max(max_len,length)
        return max_len


