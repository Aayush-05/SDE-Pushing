#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// 31. Next Permutation
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int pivot = -1;  //find pivot
        for (int i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] < nums[i+1]) {
                pivot = i;
                break;
            }
        }
        // Reverse entire array if no pivot
        if (pivot == -1){
            std::reverse(nums.begin(), nums.end());
            return;
        }
        // find element to swap with pivot
        for (int i = nums.size() -1; i > pivot; --i){
            if (nums[i] > nums[pivot]) {
                std::swap(nums[pivot], nums[i]);
                break;
            }
        }
        //reverse suffix
        std::reverse(nums.begin() + pivot + 1, nums.end());
        
    }
};