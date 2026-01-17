class Solution {
    public int majorityElement(int[] nums) {
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        int max = Integer.MIN_VALUE;
        int ans = 0;

        for(Map.Entry <Integer, Integer> entry : map.entrySet()){
            if(entry.getValue() > max){
                max = entry.getValue();
                ans = entry.getKey();
            }
        }
        return ans;
    }
}

// -------------------
//[3,2,3]
// 0 0 0 
// 3 - 2, 2 - 1