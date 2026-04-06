class Solution {
    public boolean isHappy(int n) {
        Set<Integer> s=new HashSet<>();
        while (n!=1){
            if(s.contains(n)){
                return false;
            }
            s.add(n);
            int sum=0;
            String str=String.valueOf(n);
            for(int i=0;i<str.length();i++){
                int num=str.charAt(i)-'0';
                sum+=num*num;
            }
            n=sum;
        }
        return true;
    }
}
