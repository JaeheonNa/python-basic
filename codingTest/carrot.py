xy = input()
goal_x = int(xy.split()[0])
goal_y = int(xy.split()[1])

answer = goal_x + goal_y + min(goal_x // 10, goal_y // 10)
print(answer)
