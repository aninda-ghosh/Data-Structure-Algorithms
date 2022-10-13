class Solution {
public: 
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        int m = nums1.size();
        int n = nums2.size();
        
        float *combine_arr = new float[m+n+1];
        
        
        int mid_point = 0;
        int iseven = 0;
        if((m+n)%2 == 0){
            iseven = 1;
            mid_point = floor((m+n)/2);
        }
        else {
            mid_point = (m+n+1)/2;
        }
            
        int i = 0;
        int j = 0;
        int k = 0;
        while(k<mid_point+1) {
            if (i<m && j<n) {
                if(nums1[i] < nums2[j]) {
                    combine_arr[k] = nums1[i];
                    i++;
                    k++;
                }

                else if (nums1[i] > nums2[j]) {
                    combine_arr[k] = nums2[j];
                    j++;
                    k++;
                }

                else {
                    combine_arr[k++] = nums1[i];
                    combine_arr[k] = nums2[j];
                    i++;
                    j++;
                    k++;
                }    
            }
            else if(i<m && j>=n) {
                combine_arr[k] = nums1[i];
                i++;
                k++;
                if(m+n == 1){
                    combine_arr[k++] = 0;
                }
            }
            else if(i>=m && j<n) {
                combine_arr[k] = nums2[j];
                j++;
                k++;
                if(m+n == 1){
                    combine_arr[k++] = 0;
                }
            }            
        }e
        if(iseven){
            return (combine_arr[mid_point-1] + combine_arr[mid_point]) / 2;
        }else{
            return combine_arr[mid_point-1];
        }
    }
};