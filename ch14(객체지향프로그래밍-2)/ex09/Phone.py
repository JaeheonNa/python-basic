class Phone(object):

    def __init__(self):
        self.model = ''
        self.color = ''

    def powerOn(self):
        print('전원을 켭니다.')

    def powerOff(self):
        print('전원을 끕니다.')

    def bell(self):
        print('벨이 울립니다.')

    def sendVoice(self, message):
        print('자신: ', message)

    def receiveVoice(self, message):
        print('상대: ', message)

    def hangup(self):
        print('전화를 끊습니다.')

