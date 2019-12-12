class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        if (nums1.size() > nums2.size())
            swap(nums1, nums2);
        
        int m = nums1.size(), n = nums2.size();
        int mid = (m + n + 1) / 2;
        int imin = 0, imax = m;
        
        // we do a binary search on both sorted arrays
        while (imin <= imax) {
            int i = (imin + imax) / 2;
            int j = mid - i;
            
            if (i < m && nums2[j-1] > nums1[i]) {
                // i is too small, look to the right
                imin = i + 1;
                
            } else if (i > 0 && nums2[j] < nums1[i-1]) {
                // i is too big, look to the left
                imax = i - 1;
                
            } else {
                // i is perfect
                int max_of_left;
                if (i == 0) 
                    max_of_left = nums2[j-1];
                else if (j == 0) 
                    max_of_left = nums1[i-1];
                else 
                    max_of_left = max(nums1[i-1], nums2[j-1]);
                    
                if ((m + n) % 2 == 1) return max_of_left;
                
                // m + n is even
                int min_of_right;
                if (i == m) 
                    min_of_right = nums2[j];
                else if (j == n) 
                    min_of_right = nums1[i];
                else 
                    min_of_right = min(nums1[i], nums2[j]);
                    
                return (max_of_left + min_of_right) / 2.0;
            }
        } 
        return 0.0;
    }
};
