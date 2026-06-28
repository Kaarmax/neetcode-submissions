class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        my_dict2 = {}
        if len(s) != len(t):
            return False
        for char in s:
            my_dict[char] = 0
        for char in s:
            my_dict[char] += 1
        for char in t:
            my_dict2[char] = 0
        for char in t:
            my_dict2[char] += 1
        for key in my_dict:
            if key not in my_dict2:
                return False
            elif my_dict[key] != my_dict2[key]:
                return False
        else:
            return True