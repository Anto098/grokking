def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals)-1):
        if intervals[i+1][0] < intervals[i][1]:
            return False

    return True


if __name__ == "__main__":
    print(f"Can attend all appointments {can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])}")
    print(f"Can attend all appointments {can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])}")
    print(f"Can attend all appointments {can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])}")



