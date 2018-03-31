# Start from the left of an ordered list
# Make dictionary of divisibles
#   eg: cases = [1, 2, 3, 5]
#       saved = {1: [[1]], 2: [[1, 1], [2]], 3: [[1, 2], [3]], 5: [[1, 2, 2]]}

# Start i at right and j and left and see what combos to make
# i = 5
# 5 % 1 == 0 ==> [j]*i
# 5 % 2 != 0
#   5 // 2 == divi == 2 ; rem = i % j (1)
#       rem in cases ==> [j]*(divi) + [rem]
#       if j % rem == 0 eg 2 % 1 == 0
#           [j]*(divi-1) + [rem]*(i-j*(divi-1))

# OR

# Start from right of an ordered list
# if i > num, i is ineligible
#   skip it
# if i == num, [i] is combo and cannot be combined
#   is it already in all combos? add it or skip adding
# elif i % num == 0, [i]*(num//i) is combo
#   is it already in all combos? add it or skip adding
# EITHER subtract one of i and move j right to see which other combos can make up diff
# OR subtract one of i and move j from left to see which other combos


# FIRST
#   get cache:
#   from right of list
#   cache[i] = (i // i-1, i % i-1)

def _get_case_cache(cases):
    """ Go through all cases to generate factor cache. """

    cache = {}
    cases.reverse()

    for i in range(len(cases)):
        if i == len(cases) - 1:
            cache[cases[i]] = (1, 0)
        else:
            cache[cases[i]] = (cases[i] // (cases[i+1]), cases[i] % (cases[i+1]))

# if not cases or if num < 1
# if 1 in list,
#   all_combos.append([1]*num),


# all_combos = []

# for i in range(len(cases)):
#   if cases[i] <= num:
#       combos = get_combos(num, cases[:i+1], curr_combo=[], case_combos=[])
#       all_combos.extend([combo for combo in combos if combo not in all_combos])

# this only happens during remainder calcs
# if num < 1,
#   return curr_combo
# if num < cases[0],
#   return curr_combo
# for i in range(len(cases))
#   if cases[i] > num,
#       cases[i] is ineligible,
#       next i
#   known: case[i] <= num
#   curr_combo.extend([i]*num//cases[i])
#   for n in range(1, num//cases[i]+1):
#       rem = num - cases[i]*n
#       temp_combo = get_combos(rem, cases, curr_combo, case_combos).sort()
#       if sum(temp_combo) == num and temp_combo not in case_combos:
#           case_combos.append(temp_combo)
# return case_combos

def get_all_combos(num, cases):
    """ Returns all unique combinations of cases whose sum is num. """

    cases.reverse()
    all_combos = []

    for i in range(len(cases)):
        if cases[i] <= num:
            combos = get_case_combos(num, cases[:i+1])
            all_combos.extend([cmb for cmb in combos if cmb not in all_combos])

    return all_combos


def get_case_combos(num, cases, curr_combo=[], case_combos=[]):
    """ Returns all unique combinations of cases with one required case. """

    # This only happens during remainder calcs
    if num < 1 or num < cases[0]:
        return curr_combo

    for i in range(len(cases))
        if cases[i] > num:
            # cases[i] is ineligible
            continue
        # known: case[i] <= num
        curr_combo.extend([cases[i]*num] // cases[i])
        for n in range(1, num // (cases[i]+1)):
            rem = num - cases[i] * n
            temp_combo = get_combos(rem, cases, curr_combo, case_combos).sort()
            if sum(temp_combo) == num and temp_combo not in case_combos:
                case_combos.append(temp_combo)
    return case_combos






