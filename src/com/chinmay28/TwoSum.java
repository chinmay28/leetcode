package com.chinmay28;

import java.util.HashMap;
import java.util.Map;


public class TwoSum {

    public static void main(String args[]) {
        System.out.println("Hello!");
        Map<Integer, Integer> indexMap = new HashMap();
        indexMap.put(1,2);
        indexMap.put(3,1);

        for (int key: indexMap.keySet()) {
            System.out.println("Key:" + key + " Value:" + indexMap.get(key));
        }

        new Solution().twoSum(new int[]{3,2,4}, 6);
    }
}


class Solution {

    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> indexMap = new HashMap<>(nums.length);

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (indexMap.containsKey(complement)) {
                return new int[]{i, indexMap.get(complement)};
            }
            indexMap.put(nums[i], i);
        }
        return null;
    }
}
