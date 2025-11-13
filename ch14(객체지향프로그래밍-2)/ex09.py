from DMBPhone import *

if __name__ == '__main__':
    dmbPhone = DMBPhone("Samsung", "Black", 13)

    print("모델: ", dmbPhone.model)
    print("색상: ", dmbPhone.color)
    print("채널: ", dmbPhone.channel)

    dmbPhone.powerOn()
    dmbPhone.bell()
    dmbPhone.sendVoice("안녕하세요.")
    dmbPhone.receiveVoice("네, 반갑습니다.")
    dmbPhone.hangup()

    dmbPhone.turnOnDMB()
    dmbPhone.changeDMBChannel(11)
    dmbPhone.turnOffDMB()
    dmbPhone.powerOff()


