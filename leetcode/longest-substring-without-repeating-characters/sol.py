class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        curr_len = 0
        max_len = 0

        for i in range(len(s)):
            char = s[i]
            if char in seen:
                # Remove all values that are prev to this i
                prev_occurrence_i = seen[char]
                chars_to_delete = []
                for prev_char, prev_i in seen.items():
                    if prev_i <= prev_occurrence_i:
                        chars_to_delete.append(prev_char)

                for prev_char in chars_to_delete:
                    seen.pop(prev_char)
                curr_len = i - prev_occurrence_i - 1

            curr_len += 1
            seen[char] = i

            if curr_len > max_len:
                max_len = curr_len

        return max_len


print(Solution().lengthOfLongestSubstring("dvdf"))