class Solution {
    set<vector<int>> res;
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int> perm;
        backtrack(nums, perm);
        return vector<vector<int>>(res.begin(), res.end());
    }

private:
    void backtrack(vector<int>& nums, vector<int>& perm) {
        if (perm.size() == nums.size()) {
            res.insert(perm);
            return;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != INT_MIN) {
                int temp = nums[i];
                perm.push_back(temp);
                nums[i] = INT_MIN;
                backtrack(nums, perm);
                nums[i] = temp;
                perm.pop_back();
            }
        }

    }
};