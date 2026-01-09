# 1000원, 500원, 100원 화폐 사용 가능.
# 1000원, 500원, 100원 각각의 수를 입력 받은 후, 거스름돈을 계산해 반환하는 프로그램.

item_price = int(input("물건 값을 입력하세요: "))

bills_1000 = int(input("1000원권 수: "))
coins_500 = int(input("500원권 수: "))
coins_100 = int(input("100원권 수: "))

nod_money = ((1000 * bills_1000) + (500 * coins_500) + (100 * coins_100)) - item_price

print("거스름돈: ", nod_money)

bills_1000_cnt = nod_money // 1000
nod_money = nod_money % 1000
coins_500_cnt = nod_money // 500
nod_money = nod_money % 500
coins_100_cnt = nod_money // 100

print("1000원 수: ", bills_1000_cnt)
print("500원 수: ", coins_500_cnt)
print("100원 수: ", coins_100_cnt)