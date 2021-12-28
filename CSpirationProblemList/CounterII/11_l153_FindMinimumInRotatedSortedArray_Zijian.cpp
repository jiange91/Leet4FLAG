class Solution {
public:
    int findMin(vector<int>& nums) {
        return nums[bs(nums, 0, nums.size()-1)];
    }
    
    int bs(vector<int> nums, int begin, int end) {
        while (begin < end) {
            if (nums[begin] < nums[end]) {
                return begin;
            }
            int mid = begin + (end - begin) / 2;
            if (nums[mid] < nums[begin]) {
                end = mid;
            } else if (nums[mid] > nums[end]) {
                begin = mid+1;
            } 
        }
        return begin;
    }
};
