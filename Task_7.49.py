def find_farthest_orbit(orbits):
    result = 0
    res = 0
    for i in range(len(orbits)):
        if orbits[i][0] == orbits[i][1]:
            result = result
        else:
            tmp = orbits[i][0] * orbits[i][1]
            if tmp > result:
                result = tmp
                res = orbits[i]
    return res

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(find_farthest_orbit(orbits))