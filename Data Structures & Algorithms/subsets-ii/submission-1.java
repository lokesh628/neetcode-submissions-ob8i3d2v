class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int n=nums.length;
        // Arrays.sort(nums);
        for(int i=0;i<n;i++){
            int j=i;
            for(j=0;j<n;j++){
                while(j>0 && nums[j]<nums[j-1]){
                    int temp=nums[j];
                    nums[j]=nums[j-1];
                    nums[j-1]=temp;
                    j-=1;
                }
            }
        }
        Set<List<Integer>> l=new LinkedHashSet<>();
        for (int i=0;i<(1<<n);i++){
            List<Integer> m=new ArrayList<>();
            for(int j=0;j<n;j++){
                if((i&(1<<j))!=0){
                    m.add(nums[j]);
                }
            }
        l.add(m);
        }
        return new ArrayList<>(l);
    }
}
