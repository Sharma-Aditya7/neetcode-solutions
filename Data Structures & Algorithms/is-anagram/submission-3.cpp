class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> s_counter;
        unordered_map<char, int> t_counter;

        for (int i = 0; i < s.length(); i++) {
            s_counter[s[i]]++;
            t_counter[t[i]]++;
        }
        return s_counter == t_counter;
    }
};
