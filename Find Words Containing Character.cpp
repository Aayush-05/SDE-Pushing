class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;

        for(int i = 0; i < words.size(); ++i) {
            if (words[i].find(x) != string::npos) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

//https://leetcode.com/problems/find-words-containing-character/solutions/6777583/2942-find-words-containing-character-by-jbzog
