class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> n = new HashSet<>();
        for(int num: nums){
            n.add(num);
        }
        if(n.size()==nums.length){
            return false;
        }
        else{
            return true;
        }
    }
}