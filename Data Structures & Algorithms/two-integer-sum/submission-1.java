

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();

        int difference;

        for (int i=0; i<nums.length; i++){
            difference = target-nums[i];
            if(seen.containsKey(difference)){
                int[] answer = {seen.get(difference), i};
                return answer;
            }
            seen.put(nums[i], i);
        }
        int[] a = {-1};
        return a;
    }
}
