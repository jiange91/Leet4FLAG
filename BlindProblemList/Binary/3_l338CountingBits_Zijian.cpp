class Solution {
public:
    vector<int> countBits(int n) {
        if (n == 0) return {0};
        vector<int> ans;
        ans.push_back(0);
        ans.push_back(1);
        int i = 2;
        while (i <= n) {
            if (i & 1 == 1) ans.push_back(ans[i-1] + 1);
            else ans.push_back(ans[i >> 1]);
            ++ i;
        }
        return ans;
    }
};
