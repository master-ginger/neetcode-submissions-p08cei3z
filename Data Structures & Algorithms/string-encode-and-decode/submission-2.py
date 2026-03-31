class Solution:

    def encode(self, strs: List[str]) -> str:
        size=[]
        if len(strs)<1:
            return ""

        for i in range(len(strs)):
            size.append(len(strs[i]))
        res=""
        for i in range(len(strs)):
            res+=str(size[i])
            res+=','
        res+='#'
        for i in range(len(strs)):
            res+=strs[i]
        return res
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes=[]
        res=[]
        i=0
        while s[i]!='#':
            curr=""
            while s[i]!=',':
                curr+=s[i]
                i+=1
            sizes.append(int(curr))
            i+=1
        i+=1 #because there is hash symbol
        for sz in sizes:
            res.append(s[i:i+sz])
            i+=sz
        return res



