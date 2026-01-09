forest = input()
forests = list(forest)

rear_leg_cnt = 0
answer = 0

for f in range(len(forests)-1):
    if forests[f] == forests[f+1]:
        if forests[f] == "(":
            rear_leg_cnt += 1
        elif forests[f] == ")":
            answer += rear_leg_cnt

print(answer)

