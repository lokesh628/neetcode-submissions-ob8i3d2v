class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int n=nums.length;
        Arrays.sort(nums);
        Set<List<Integer>> l=new HashSet<>();
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
