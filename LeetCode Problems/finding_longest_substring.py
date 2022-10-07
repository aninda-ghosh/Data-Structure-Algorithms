from collections import Counter


def lengthOfLongestSubstring_on3(s):
    if len(s) > 0:
        # First let's find all the substring from the string
        hash_map = {}
        queue = []
        substring_len = []
        removed_key_index = 0
        for i in range(0, len(s)):
            keyword = s[i]
            if keyword not in hash_map:
                # Here we need to push the keywords in the hashmap
                hash_map[keyword] = i
                queue.append(keyword)
            else:
                # We found some duplicates
                # print "Duplicates in :", keyword, hash_map[keyword]
                for k in range(0, hash_map[keyword] + 1 - removed_key_index):
                    if (len(queue) > 0):
                        queue.pop(0)
                        removed_key_index += 1
                hash_map[keyword] = i
                queue.append(keyword)
            substring_len.append(len(queue))
        if len(queue) > 0:
            substring_len.append(len(queue))
            return max(substring_len)
    else:
        return 0


def lengthOfLongestSubstring_2n(s):
    if len(s) > 0:
        freq_dict = Counter()
        left, right = 0, 0
        max_len = 0

        # Using Sliding Window Approach and Hash Map to track the frequencies of the characters
        # Iterating over the sequence to expand the window
        while right < len(s):
            right_pointer_element = s[right]
            freq_dict[right_pointer_element] += 1

            # Iterating over the sequence to minimize the window
            while freq_dict[right_pointer_element] > 1:
                left_pointer_element = s[left]
                left += 1
                freq_dict[left_pointer_element] -= 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


if __name__ == "__main__":
    String = "abcabcbb"
    print("Longest 2n: ", lengthOfLongestSubstring_2n(String))
    print("Longest On3: ", lengthOfLongestSubstring_on3(String))

