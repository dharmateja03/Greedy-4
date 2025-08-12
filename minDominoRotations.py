# TimeComplexity:O(2*n)
# SpaceComplexity:O(1)
# Appraoch:
# Brute force way would be checking for all number number either they shjould exist in top or bottom then only it would be possible
# optimal we can use freq map to get number which is repeated >=n then check for each top and bottom
# optimal with optimal space if you obbserve either top number or bottom number should be a number which is repated else it is not possible based on that fact take both top and bottom number 
# then check

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        at,ab=0,0
        """
        here we can only swaps a[i],b[i]we cannot swao ohter, 
        observations would be if freq of a num should be >=n
        """
        # print(d)
        # print(k)
        k=tops[0]
        n=len(tops)
        b=True
        for i in range(n):
            if tops[i]==k and bottoms[i]!=k:
                ab+=1
            elif bottoms[i]==k and tops[i]!=k:
                at+=1
            elif  bottoms[i]==k and tops[i]==k:continue
            else:
                b=False
                break
        if b:
            return min(at,ab)
        k=bottoms[0]
        b=True
        at,ab=0,0
        for i in range(n):
            if tops[i]==k and bottoms[i]!=k:
                ab+=1
            elif bottoms[i]==k and tops[i]!=k:
                at+=1
            elif  bottoms[i]==k and tops[i]==k:continue
            else:
                b=False
                break
        if b:
            return min(at,ab)
        return -1
        
