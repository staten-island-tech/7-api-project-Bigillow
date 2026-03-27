def streak(trees):
    streak_inc = 1
    streak_dec = 1 
    high = [1]
    low = [1]
    for i in range(len(trees)-1):
        if trees[i] < trees[i + 1]:
            streak_inc += 1
            streak_dec = 1 
            high.append(streak_inc)
        elif trees[i] > trees[i + 1]:
            streak_dec += 1
            streak_inc = 1
            low.append(streak_dec)
    print(max(high))
    print(max(low))

        
streak("1243")
