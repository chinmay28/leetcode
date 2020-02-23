
/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
*/


#include<iostream>
#include<stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (int i=0; i<s.length(); i++) {
            
            bool pop = false;
            if (!stk.empty())                
                pop = (s[i] == ')' && stk.top() == '(') || 
                    (s[i] == '}' && stk.top() == '{') || 
                    (s[i] == ']' && stk.top() == '[');                

            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                stk.push(s[i]);
            
            else if (pop)
                stk.pop();
            else
                return false;
        }
        
        if (stk.empty())
            return true;
        else
            return false;
    }
};
