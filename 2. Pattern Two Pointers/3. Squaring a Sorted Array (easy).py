def make_squares(arr):
    arr = [i ** 2 for i in arr]
    start, end = 0, len(arr) - 1
    new_arr = []
    while start <= end:
        if arr[start] <= arr[end]:
            new_arr.append(arr[end])
            end -= 1
        else:
            new_arr.append(arr[start])
            start += 1

    return new_arr[::-1]


if __name__ == "__main__":
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
