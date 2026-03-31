class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        flag=True
        for i in s:
            if i not in dic1:
                dic1[i]=1
            else:
                dic1[i]+=1
        
        for i in t:
            if i not in dic2:
                dic2[i]=1
            else:
                dic2[i]+=1
        
        for i in s:
            if i in dic1 and i in dic2:
                if dic1[i]!=dic2[i]:
                    flag=False
            else:
                flag=False
        for i in t:
            if i in dic1 and i in dic2:
                if dic1[i]!=dic2[i]:
                    flag=False
            else:
                flag=False
        print(dic1,dic2)
        if flag:
            return True
        else:
            return False
