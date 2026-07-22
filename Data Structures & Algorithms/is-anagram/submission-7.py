class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 dict, s_dict and t_dict
        s_dict, t_dict = {}, {}
        # check len s and len t are same
        if len(s) == len(t):
            # traverse the list, for loop
            for i in range(len(s)):
                # if s_dict not empty and s[i] in s_dict:
                if s[i] in s_dict:
                    # s_dict[s[i]] = +1
                    s_dict[s[i]] = s_dict[s[i]] + 1
                else:
                    # set s[i] as key, set it's value to 0 
                    s_dict[s[i]] = 0
                # if t_dict not empty and t[i] in t_dict:
                if t[i] in t_dict:
                    # t_dict[key] = +1
                    t_dict[t[i]] = t_dict[t[i]] + 1
                else:
                    # set t[i] as key, set it's value to 0 
                    t_dict[t[i]] = 0
            # return s_dict == t_dict
            return s_dict == t_dict
        # else false
        else: 
            return False
