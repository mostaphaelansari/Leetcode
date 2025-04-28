class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Map to store numbers and their indices.
        Map<Integer, Integer> map = new HashMap<>();
        
        // Iterate over the array.
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            // If the complement exists, return the indices.
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            // Otherwise, store the current number and its index.
            map.put(nums[i], i);
        }
        // If no solution is found (though the problem guarantees one), throw an exception.
        throw new IllegalArgumentException("No two sum solution");
    }
}