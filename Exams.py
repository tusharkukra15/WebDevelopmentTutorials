def customCompare(exam_date1, exam_date2):

    if exam_date1[0] == exam_date2[0]:
        return exam_date1[1] - exam_date2[1]
    else:
        return exam_date1[0] - exam_date2[0]


def solve(exam_dates):

    # sort by actual date of exams
    exam_dates.sort(cmp=customCompare)

    last_exam_date = exam_dates[0][1]

    for i in xrange(1, len(exam_dates)):

        actual_date = exam_dates[i][0]
        early_date = exam_dates[i][1]

        if early_date >= last_exam_date:
            last_exam_date = early_date
        else:
            last_exam_date = actual_date

    return last_exam_date


if __name__ == "__main__":

    t = int(raw_input())

    exam_dates = list()
    for _ in xrange(0, t):
        a, b = map(int, raw_input().split(" "))
        exam_dates.append([a, b])

    print solve(exam_dates)
