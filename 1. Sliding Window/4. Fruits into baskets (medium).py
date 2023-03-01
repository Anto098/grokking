def fruits_into_baskets(fruits):
    start = 0
    chars = {}
    _max = 0

    for end in range(len(fruits)):
        if fruits[end] not in chars or chars[fruits[end]] == 0:
            chars[fruits[end]] = 0
        chars[fruits[end]] += 1

        while len(chars) > 2:
            chars[fruits[start]] -= 1
            if chars[fruits[start]] == 0:
                del chars[fruits[start]]
            start += 1

        _max = max(_max, end - start + 1)

    return _max


if __name__ == "__main__":
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
