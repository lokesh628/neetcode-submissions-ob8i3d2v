class Solution {
    public int maxProduct(int[] nums) {
        int n=nums.length;
        int pref=1;
        int suff=1;
        int mx=Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            pref=pref*nums[i];
            suff=suff*nums[n-i-1];
            mx=Math.max(mx,Math.max(pref,suff));
            if (suff==0){
                suff=1;
            }
            if(pref==0){
                pref=1;
            }
        }
        return mx;
    }
}
