class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n=nums.length;
        List<Integer> l=new ArrayList<>();
        for(int i=0;i<=n-k;i++){
            int mx=Integer.MIN_VALUE;
             for(int j=i;j<i+k;j++){
                mx=Math.max(mx,nums[j]);
             }
             l.add(mx);
        }
        int a[]=new int[l.size()];
        for(int i=0;i<l.size();i++){
            a[i]=l.get(i);
        }
        return a;
    }
}
