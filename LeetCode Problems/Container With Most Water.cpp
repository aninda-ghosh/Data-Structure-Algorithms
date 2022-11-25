class Solution {
public:
    int min(int a, int b) {
        if(a<b) return a;
        else return b;
    }
    
    int max(int a, int b) {
        if(a>b) return a;
        else return b;
    }
    
    int maxArea(vector<int>& height) {
        int ptr1 = 0;
        int ptr2 = height.size()-1;
        
        int max_area = 0;
        int curr_area = 0;
        
        while(ptr1 != ptr2) {
            curr_area = (ptr2-ptr1) * min(height[ptr1], height[ptr2]);
            max_area = max(curr_area, max_area);
            if(height[ptr1] < height[ptr2]){
                ptr1++;
            }
            else{
                ptr2--;    
            }
            // printf("Area->%d, ptr1->%d, ptr2->%d\n", max_area, ptr1, ptr2);
        }        
        return max_area;
    }
};