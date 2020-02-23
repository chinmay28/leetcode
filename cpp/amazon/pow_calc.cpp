
/*
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
*/

#include<iostream>


class Solution {
public:
    
    double fastPower(double x, long long n) {
        if (n == 0)
            return 1.0;
        
        double half_result = fastPower(x, n/2);
        if (n % 2 == 1)
            return x * half_result * half_result;
        else
            return half_result * half_result;
    }
    
    double myPow(double x, int n) {
    
        long long exp = n;
        if (n < 0) {
            exp = -exp;
            x = 1/x;
        }
            
        return fastPower(x, exp);
    }
};
