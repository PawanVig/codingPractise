class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++)
        {
            int delta = target- nums[i];
            if(map.containsKey(delta))
            {
                return new int [] {map.get(delta),i};
            }
            map.put(nums[i],i);
        }
        return null;
    }
}