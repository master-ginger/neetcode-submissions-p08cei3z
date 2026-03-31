class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        n=len(s)
        m=len(t)
        if n>m:
            for i in range(m):
                if t[i] in dic:
                    dic[t[i]]+=1
                else:
                    dic[t[i]]=1
            for i in range(n):
                if s[i] in dic and dic[s[i]]>0:
                    dic[s[i]]-=1
                else:
                    return False
            
        else:
            for i in range(n):
                if s[i] in dic:
                    dic[s[i]]+=1
                else:
                    dic[s[i]]=1
            for i in range(m):
                if t[i] in dic and dic[t[i]]>0:
                    dic[t[i]]-=1
                else:
                    return False
        return True   
        

        
