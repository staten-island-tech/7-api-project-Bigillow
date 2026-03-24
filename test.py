def streak(trees):
    wasd = int(trees)
    streak_inc = 0
    streak_dec = 0 
    lowest = max(wasd)
    highest = 0 
    high = []
    low = []
    for tree in trees:
        if tree > highest:
            highest = tree
            streak_inc += 1
        elif tree < highest:
            high.append(streak_inc)
            streak_inc = 0
            streak_dec += 1
        if tree > lowest:
            lowest = tree
            streak_dec += 1
        elif tree < lowest:
            low.append(streak_dec)
            streak_dec = 0
            streak_inc += 1
        
streak("1 3 4 2")
