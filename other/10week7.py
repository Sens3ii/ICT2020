set1 = {10, 20, 30, 40, 50}

set2 = {60, 70, 80, 90, 10}

final_set = set1.intersection(set2)

if len(final_set) == 0:
    print("Two sets have no items in common")
else:
    print("Two sets have items in common:", final_set, sep="\n")
