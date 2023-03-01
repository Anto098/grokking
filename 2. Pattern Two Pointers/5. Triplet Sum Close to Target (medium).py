def triplet_sum_close_to_target(l, target_sum):
    l.sort()
    triplet_sum = sum([l[0], l[1], l[2]])  # there will always only be one

    len_l = len(l)
    for i in range(len_l - 1):
        if i > 0 and l[i] == l[i - 1]:
            continue

        start = i + 1
        end = len_l - 1
        while start < end:
            curr_sum = l[i] + l[start] + l[end]

            delta_ts_cs = abs(target_sum - curr_sum)
            delta_ts_ts = abs(target_sum - triplet_sum)
            
            if delta_ts_cs < delta_ts_ts:
                triplet_sum = curr_sum
            elif delta_ts_cs == delta_ts_ts:
                triplet_sum = min(curr_sum, triplet_sum)

            if curr_sum == target_sum:
                start += 1
                end -= 1
                while start > 0 and l[start] == l[start - 1]:
                    start += 1
                while end < len_l - 1 and l[end] == l[end + 1]:
                    end -= 1

            elif curr_sum < target_sum:
                start += 1
            else:
                end -= 1

    return triplet_sum


if __name__ == "__main__":
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
