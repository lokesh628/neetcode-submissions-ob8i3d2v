class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        n=len(arr)
        li=[]
        i=0
        while(i<n):
            j=i+1
            while(j<n):
                x=arr[i]+arr[j]
                if(x==target):
                    li.append(i+1)
                    li.append(j+1)
                j+=1
            i+=1
        return li