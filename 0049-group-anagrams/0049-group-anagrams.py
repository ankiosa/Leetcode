from string import ascii_lowercase


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        list_anagram_group = []
        each_num_dict = {}
        dict_eng = {v:k for k,v in enumerate(ascii_lowercase)}
        i =0
        for each_word in strs:
          base_str = [0]*26
          for each_char in each_word:
            base_str[dict_eng[each_char]] += 1
          print(base_str)
          final_str = "-".join(map(str,base_str))
          if(final_str in each_num_dict):
            list_anagram_group[each_num_dict[final_str]].append(each_word)
          else:
            each_num_dict[final_str] = i
            i = i+1
            list_anagram_group.append([each_word])
        return sorted(list_anagram_group)

            



