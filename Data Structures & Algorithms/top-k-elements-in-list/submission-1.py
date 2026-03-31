class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}

        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        res=[]
        keys=[]
        for key in dic:
            keys.append(key)
        # print(keys)
        print(dic)
        for i in range(k):
            max1=0
            maxi=0
            for j in keys:
                if dic[j]>max1:
                    max1=dic[j]
                    maxi=j
            res.append(maxi)
            keys.remove(maxi)
            print(keys)
        return res