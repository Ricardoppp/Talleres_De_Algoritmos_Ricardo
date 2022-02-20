while True:
    M, XP = input().split(" ")
    XP = int(XP)
    M = int(M)
    if XP == 0 and M == 0:
        break
    else:
        XP_A = M * XP
    print(XP_A)
