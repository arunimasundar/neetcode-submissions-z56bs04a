class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s)<len(t):
            return ""

        tdict=Counter(t)
        print(tdict)
        chars_remaining = len(t)
        min_window=(0,float("inf"))
        l=0  
        for r,ch in enumerate(s):
            # print("tdict",tdict)
            if tdict[ch]>0:
                chars_remaining-=1
            tdict[ch]-=1
            # print("first",tdict)
            if chars_remaining==0:
                while True:
                    temp = s[l]
                    if(tdict[temp]==0):
                        break
                    tdict[temp]+=1
                    l+=1
                    # print("second",tdict)
                if r-l < min_window[1] - min_window[0]:
                    min_window=(l,r)
                    print(min_window)
                tdict[s[l]]+=1
                chars_remaining+=1
                l+=1
        return "" if min_window[1]>len(s) else s[min_window[0]:min_window[1]+1]
