def isWin(card):
    main_diag = 0
    second_diag = 0
    row = 0
    for i in card.values():
        if (i.count(0) == 5):
            return True
        main_diag += i[row]
        second_diag += i[4 - row]
        row += 1

    if (main_diag == 0 or second_diag == 0):
        return True

    for i in range(5):
        temp = 0
        for j in card.values():
            temp += j[i]
        if (temp == 0):
            return True
    return False