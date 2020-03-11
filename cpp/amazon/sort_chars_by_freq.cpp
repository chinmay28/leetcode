/**
 * 
 * Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 * 
 * **/

#include<iostream>
#include<unordered_map>
#include<queue>
using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        string result;
        unordered_map<char, int> counter;
        
        for (int i=0; i<s.length(); i++) {
            counter[s[i]] += 1;
        }
        
        priority_queue<pair<int, char> > char_queue;
        
        for (auto it=counter.begin(); it != counter.end(); ++it) {
            char_queue.emplace(pair<int, char> (it->second, it->first));
        }
        
        while (!char_queue.empty()) {
            pair<int, char> item = char_queue.top();
            char_queue.pop();
            
            for (int i=0; i<item.first; i++) {
                result += item.second;
            }
        }
        
        return result;
    }
};
