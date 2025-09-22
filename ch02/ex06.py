# 초를 입력 받아서 시, 분, 초로 변경하는 프로금램

time = int(input("초를 입력하세요. : "))

second = time % 60
minute = (time // 60) % 60
hour = (time // 60 ) // 60

print(hour, " 시 ", minute, " 분 ", second, " 초 ")