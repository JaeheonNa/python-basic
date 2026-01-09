import os
import time
import threading
from thread.Ping import *
from thread.Diring import *

print("---싱글 스레드---")
print("비프음이 다 울리고 난 뒤 콘솔 로그가 찍힘")
for i in range(3):
    print("현재 실행중인 스레드명(첫 번째 for문): ", threading.current_thread().name)
    os.system('afplay /System/Library/Sounds/Ping.aiff')

for i in range(3):
    print("현재 실행중인 스레드명(두 번째 for문): ", threading.current_thread().name)
    print("띠링~")
    time.sleep(1)

print("---멀티 스레드---")
print("비프음이 울림과 동시에 콘솔 로그가 찍힘")
ping = Ping("Ping")
ping.start()
for i in range(3):
    print("띠링~")
    time.sleep(2.3)
