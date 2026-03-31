class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=s.split(" ")
        t="".join(arr)
       
        m=""
        for i in t:
            
            if i.isalpha() or i.isdigit():
                m+=i.lower()
            

        a=m[::-1]
        print(a)
        print(m)
        if a==m:
            return True
        else:
            return False