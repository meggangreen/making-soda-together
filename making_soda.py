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


def get_case_combos(num, cases, curr_combo=[], case_combos=[]):
    """ Returns all unique combinations of cases with one required case. """

    # This only triggers during remainder calcs
    # if not cases or num < 1 or num < cases[0]:
    #     return None

    for i in range(len(cases)):
        if cases[i] > num:
            # cases[i] is ineligible
            continue
        # known: case[i] <= num
        dividend = num // cases[i]
        print("curr, num before for loop", curr_combo, num)
        for n in range(0, dividend + 1):
            # print("curr in for loop before extend", curr_combo)
            # if curr_combo:
            curr_combo.extend([cases[i]] * (dividend - n))
            # else:
            #     curr_combo = [cases[i]] * (dividend - n)
            rem = num - sum(curr_combo)
            print("curr, num, rem in for loop after extend", curr_combo, num, rem)
            # import pdb; pdb.set_trace();
            if rem < 0:
                break
            elif rem > 0 and len(cases) > 1:
                get_case_combos(rem, cases[i+1:], curr_combo)
            elif sum(curr_combo) == num and curr_combo not in case_combos:
                case_combos.append(curr_combo)
                curr_combo = []
                print("case combos, num, rem", case_combos, num, rem)

    return case_combos


            # temp_combo = get_case_combos(num, cases[i+1:], curr_combo)
            # print("temp after return", temp_combo)
            # curr_combo = curr_combo + temp_combo if temp_combo else curr_combo
            # print("curr in for loop after addition", curr_combo)
if __name__ == '__main__':
    print(get_case_combos(4, [3, 2, 1]))




