"""
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        #return self.backtrack(arr, 0, '', 0)
        return self.dp_using_sets(arr)

    def backtrack(self, string_list, i, current_string, result):

        if i == len(string_list):
            # we have reached the end of the string list
            result = max(result, len(current_string))
            return result

        if len(set(string_list[i])) == len(string_list[i]):
            # ith string has unique characters
            if all(char not in current_string for char in string_list[i]):
                result = self.backtrack(string_list, i + 1,
                                        current_string + string_list[i], result)

        result = self.backtrack(string_list, i+1, current_string, result)
        return result

    def dp_using_sets(self, array):

        dp = [set()]
        for string in array:
            if len(set(string)) != len(string):
                continue
            for dp_string_set in dp:
                if not dp_string_set & set(string):
                    dp.append(dp_string_set | set(string))

        return max(len(string_set) for string_set in dp)


