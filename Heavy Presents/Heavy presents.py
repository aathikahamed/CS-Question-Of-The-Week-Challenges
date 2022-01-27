input()
weights = [int(weight) for weight in input().split(' ')]
questions = [input() for _ in range(int(input()))]

sums = {}

for question in questions:

    indexes = question.split(' ')
    beginning, end = [int(index) for index in indexes]
    beginning -= 1
    if beginning in sums:
        # if beginning and end are in the sums
        if end in sums[beginning]:
            print(sums[beginning][end])
            continue
        # if beginning is in the sums but end is not
        other_end, other_sum = sums[beginning].popitem()
        if other_end > end:
            s = other_sum - sum(weights[end:other_end])
        else:
            s = other_sum + sum(weights[other_end:end])
        sums[beginning] = {other_end: other_sum, **sums[beginning], end: s}
        print(s)
        continue

    end_found = False

    # if beginning is not in the sums
    for i in sums.items():
        # if end is in the sums, but beginning is not
        if end in i[1]:
            end_found = True
            other_index = i[0]
            if other_index > beginning:
                s = i[1][end] + sum(weights[beginning:other_index])
            else:
                s = i[1][end] - sum(weights[other_index:beginning])
            sums[beginning] = {end: s}
            print(s)
            break
    if end_found:
        continue

    s = sum(weights[beginning:end])
    sums[beginning] = {end: s}
    print(s)

# 6
# 5 7 8 2 10 34
# 4
# 1 3
# 1 4
# 2 3
# 3 5
