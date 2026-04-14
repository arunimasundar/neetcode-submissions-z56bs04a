from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        res=0
        l=0
        for r in range(len(s)):
            freq[s[r]]+=1
            maxfreq= max(freq.values())
            currWinLen=r-l+1
            if(currWinLen - maxfreq>k):
                freq[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res


