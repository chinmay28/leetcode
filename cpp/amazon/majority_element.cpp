/*
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
*/

#include<iostream>
#include<map>
#include<vector>
using namespace std;


class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> counts;
        for (int i=0; i<nums.size(); i++) {
            counts[nums[i]] += 1;
            
            if (counts[nums[i]] > nums.size()/2)
                return nums[i];
        }
        
        return -1;
    }
};