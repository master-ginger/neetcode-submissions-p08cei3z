class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        n=len(nums)
        for i in range(n):
            if nums[i] in dictionary:
                dictionary[nums[i]]+=1
            else:
                dictionary[nums[i]]=1
        
        sorted_dic = dict(sorted(dictionary.items(),key=lambda item:item[1],reverse=True))
        print(sorted_dic)
        res=[]
        for key,value in sorted_dic.items():
            if k==0:
                break
            res.append(key)
            k-=1

        return res
        