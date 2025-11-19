from ConcreteContentsSender import *
from KakaoSender import *

if __name__ == '__main__':
    cs = ConcreteContentsSender("폭싹 속았수다", "아이유", "1화")
    cs.sendMessage("나재헌")

    print("--"*10)
    kakao = KakaoSender("카카오톡", "나재헌")
    kakao.sendMessage("아이유", "안녕하세요")