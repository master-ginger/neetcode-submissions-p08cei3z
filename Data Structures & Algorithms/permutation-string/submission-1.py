class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))
        n=len(s1)
        for i in range(len(s2)-n+1):
            print(s2[i:i+n])
            sorted_s2="".join(sorted(s2[i:i+n]))
            if sorted_s1==sorted_s2:
                return True
        return False                                                                                                                                            