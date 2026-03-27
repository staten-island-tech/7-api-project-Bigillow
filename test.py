def streak(trees):
    wasd = trees
    streak_inc = 1
    streak_dec = 2 
    lowest = max(wasd)
    highest = 0 
    high = [1]
    low = [1]
    for tree in wasd:
        if int(tree) > int(highest) and int(tree) != int(lowest):
            highest = tree
            streak_inc += 1
        elif int(tree) < int(highest) and int(tree) < int(lowest):
            lowest = tree
            highest = 0
            high.append(streak_inc)
            streak_inc = 1
            streak_dec += 1
        elif tree < lowest:
        elif int(tree) > int(highest) and int(tree) > int(lowest):
            highest = tree
            lowest = 0
            low.append(streak_dec)
            streak_dec = 2
            streak_inc += 1

    print(max(high))
    print(max(low))
        
streak("1342")
