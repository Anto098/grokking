def longest_substring_with_k_distinct(s, k):
    start = 0
    _max = 0
    chars = {}
    nb_chars = 0

    for end in range(len(s)):
        if s[end] not in chars or chars[s[end]] == 0:
            chars[s[end]] = 1
            nb_chars += 1
        else:
            chars[s[end]] += 1

        while nb_chars > k:
            chars[s[start]] -= 1
            if chars[s[start]] == 0:
                nb_chars -= 1
            start += 1

        # nb_chars == k is forced here
        _max = max(_max, (end - start + 1))

    return _max


if __name__ == "__main__":
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))
