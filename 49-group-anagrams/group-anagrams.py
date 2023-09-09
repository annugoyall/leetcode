class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        # def isAnagram(str1, str2):
        #     if len(str1) != len(str2):
        #         return False
            
        #     if str1 == str2:
        #         return True

        #     char_dict = dict()

        #     for i in str1:
        #         if i in char_dict:
        #             char_dict[i] += 1
        #         else:
        #             char_dict[i] = 1

        #     for i in str2:
        #         if i not in char_dict:
        #             return False
        #         char_dict[i] -= 1

        #     return set(char_dict.values()) == {0}

        for string in strs:
            found = False
            sorted_str = "".join(sorted(i for i in string))
            for curr_anagram in ans:
                if curr_anagram == sorted_str:
                    found = True
                    ans[curr_anagram].append(string)
                    break
            if not found:
                ans[sorted_str] = [string]
        
        return ans.values()

