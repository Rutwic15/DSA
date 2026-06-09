class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int mini = INT_MAX, maxi = INT_MIN;
        for(auto &it: nums){
            mini = min(mini, it);
            maxi = max(maxi, it);
        }
        long long ans = abs(mini - maxi);
        return k * ans;
    }
};