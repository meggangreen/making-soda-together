def make_soda(num, sizes):
    """take in number and soda sizes, output combos"""
    combos = []
    temp = []
    rem = 1
    sizes = sizes[::-1]
    # need to start at right and check for first set of sizes
    for i in range(len(sizes)):
        item = sizes[i]
        if item <= num:
            if num % item == 0:
                pack = num / item
                while pack > 0:
                    temp.append(item)
                    pack -= 1
                break
            else:
                temp.append(item)
                rem = num % item
                num = rem
    return temp
    # if temp not in combos:
    #     combos.append(temp)
    # refactor to go again
    # keep those in combo list, check if in combo list

    return combos
# print make_soda(4, [1, 2, 3])
# print make_soda(4, [2, 4])
# [[1,1,1,1], [1,1,2], [1,3], [2, 2]]


def get_all_combos(num, sizes):

    all_combos = []
    for i in range(len(sizes)):
        new_combo = make_soda(num, sizes[:i+1])
        print num, sizes[:i+1], new_combo
        all_combos.append(new_combo)

    return all_combos






def all_soda(num, sizes):
    """take in number and soda sizes, output combos"""
    combos = []
    temp = []
    rem = 1
    # sizes = sizes[::-1]

    for i in range(len(sizes)):
        item = sizes[i]
        if num % item == 0:
            pack = num / item
            temp.extend([item]*pack)
            # while pack > 0:
            #     temp.append(item)
            #     pack -= 1
        else:
            if item <= num:
                temp.append(item)
                rem = num % item
                num = rem
                # recursive call all_soda here, passing num and
                # the sliced list up to this 'i'
        combos.append(temp)

    return combos

