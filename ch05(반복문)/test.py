sol = 366
sol_cnt = 834
schd = 1449
schd_cnt = 98
year = 20

for i in range(year):
    sol *= 1.1

for i in range(year):
    schd *= 1.1

print(year, "년 후 sol", sol_cnt, "주의 배당금은 연", f'{round(sol * sol_cnt):,}', "원")
print(year, "년 후 schd",schd_cnt, "주의 배당금은 연", f'{round(schd * schd_cnt):,}', "원")
total = round(sol * sol_cnt) + round(schd * schd_cnt)
print("총", f'{total:,}', "원")