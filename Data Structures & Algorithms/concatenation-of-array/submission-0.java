class Solution {
    public int[] getConcatenation(int[] nums) {
        int n=nums.length;
        int a[]=new int[2*n];
        int temp=n;
        for(int i=0;i<n;i++){
            a[i]=nums[i];
            a[temp]=nums[i];
            temp++;
        }
        return a;
    }
}