class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ds1 = Counter(s1)
        k=len(s1)
        for r in range(len(s2)):
            # print("first",ds1)
            if s2[r] in ds1:
                ds1[s2[r]]-=1
                # print("second",ds1)
            if r>=k and s2[r-k] in ds1:
                ds1[s2[r-k]]+=1
                # print("third",ds1)
            if all([ds1[i] == 0 for i in ds1]): 
                return True
        return False