def non_repeat_substring_1(s):
    _max = 0
    start = 0
    chars = set()

    for end in range(len(s)):
        if s[end] not in chars:
            chars.add(s[end])
        else:
            while True:
                start += 1
                if s[start - 1] == s[end]:
                    break
                else:
                    chars.remove(s[start - 1])

        _max = max(_max, end - start + 1)

    return _max


def non_repeat_substring_2(s):
    _max = 0
    start = 0
    chars_map = {}

    for end in range(len(s)):
        if s[end] in chars_map:
            start = chars_map[s[end]] + 1

        chars_map[s[end]] = end

        _max = max(_max, end - start + 1)

    return _max

if __name__ == "__main__":
    print(non_repeat_substring_1("aabccbb"))
    print(non_repeat_substring_1("abbbb"))
    print(non_repeat_substring_1("abccde"))

    print("=====================")

    print(non_repeat_substring_2("aabccbb"))
    print(non_repeat_substring_2("abbbb"))
    print(non_repeat_substring_2("abccde"))
