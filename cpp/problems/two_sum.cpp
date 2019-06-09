/*
https://leetcode.com/problems/two-sum/

1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/
#include<iostream>
#include<map>
#include<vector>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> indexMap;
        vector<int> result;
        
        for (int i=0; i < nums.size(); i++) {

            int complement = target - nums[i];            
            if (indexMap.end() != indexMap.find(complement)) {
                result.push_back(indexMap[complement]);
                result.push_back(i);
                break;
            } else {
                indexMap[nums[i]] = i;
            }
        }
        return result;
    }
};


int main() {
    vector<int> numbers = {2, 7, 11, 15}; 
    vector<int> result = Solution().twoSum(numbers, 9);

    cout << result[0] << ", " << result[1] << endl;
    return 0;
}