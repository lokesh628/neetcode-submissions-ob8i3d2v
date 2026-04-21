class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        i,j=0,n-1
        c=0
        while i<=j:
            rem=limit-people[j]
            c+=1
            j-=1
            if rem>=people[i]:
                i+=1
        return c
            