import time
import module.fibo as fibo

# 1970년 1월 1일 자정 이후 지금까지 흐른 절대 시간을 초 단위로 출력
print(time.time())
start = time.time()
time.sleep(2)
end = time.time()
print("실행 시간:", end - start)
print("--" * 10)

print("현재 날짜 및 시간(문자열):", time.asctime())
print("--" * 10)

for i in range(10, 0, -1):
    print(i, end=' ')
    time.sleep(1)
print("로켓 발사!")
