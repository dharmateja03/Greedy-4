# TimeComplexity:O(nlogk)
# SpaceCompelxity:O(n)
# Approach:
# Obseravtions if a char is not in source then for sure we have to return -1 and if source has all chars that target has then worst case would be len of taget i.e all chanrs indi
# have two pointer if same inc both otherwise just inc source if gopes out of bounds reset to 0 we optize this by having index map+Binary serach

#----------------------
# using Binary search , O(nlopk)
#----------------------



class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        d=defaultdict(list)
        def bs(nums,t):
            l=0
            h=len(nums)-1
            ans=len(nums)
            while(l<=h):
                # print(l,h)
                m=(l+h)//2
                
                if nums[m]>=t:
                    ans=m
                    h=m-1
                else:
                    l=m+1
            return ans

        for i in range(len(source)):
            d[source[i]].append(i)
        sidx=0
        tidx=0
        tLen=len(target)
        sLen=len(source)
        ans=0
        while(tidx<tLen):
            if target[tidx] not in d:return -1
            temp = bs(d[target[tidx]], sidx)
            if temp == len(d[target[tidx]]):
                ans += 1
                sidx = d[target[tidx]][0] + 1
                tidx += 1
            else:
                # Found valid position
                sidx = d[target[tidx]][temp] + 1
                tidx += 1
                
                # Check if we need to start new subsequence
                if sidx >= sLen and tidx < tLen:
                    ans += 1
                    sidx = 0
        return ans+1


#-----------------------
# using hashmap
#----------------------

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s=set()
        for i in source:
            s.add(i)
        sLen=len(source)
        ans=0
        tLen=len(target)
        sidx=0
        tidx=0
        while(tidx<tLen):
            print(sidx,tidx)
            if target[tidx] not in s:return -1
            if source[sidx]==target[tidx]:
                sidx+=1
                tidx+=1
                if sidx==sLen and tidx!=tLen :
                    ans+=1
                    sidx=0
                if tidx==tLen and  sidx!=sLen :
                    ans+=1
                    return ans
                elif tidx==tLen and  sidx==sLen :
                    return ans+1
            elif source[sidx]!=target[tidx]:
                sidx+=1
                
                if sidx==sLen:
                    ans+=1
                    sidx=0
                    
        return ans
                



