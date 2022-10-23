def permutation(lst):
    l = []

    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i + 1:]

        for p in permutation(remLst):
            l.append([m] + p)
    return l

print(permutation([1,2,3,4]))