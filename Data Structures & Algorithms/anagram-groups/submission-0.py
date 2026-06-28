class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        strs_copy = strs.copy()
        L = []
        print(strs)
        print(strs_copy)

        for i, string in enumerate(strs):
            new = "".join(sorted(string))
            strs[i] = new
            if new not in my_dict:
                my_dict[new] = [i]
            else:
                my_dict[new].append(i)

        for key, value in my_dict.items():
            ls = []
            for i in value:
                ls.append(strs_copy[i])
            L.append(ls)
        return(L)
