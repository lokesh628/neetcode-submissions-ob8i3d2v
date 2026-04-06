class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l=[]
        tar=0
        for i in range(0,len(arr)-2):
            j=i+1
            k=len(arr)-1
            while(j<k):
                if(arr[i]+arr[j]+arr[k]==tar):
                    l1=[]
                    l1.append(arr[i])
                    l1.append(arr[j])
                    l1.append(arr[k])
                    l.append(tuple(l1))
                    j+=1
                    k-=1
                elif(arr[i]+arr[j]+arr[k]>tar):
                    k-=1
                else:
                    j+=1
        s=set(l)
        x=[list(i) for i in s]
        return x