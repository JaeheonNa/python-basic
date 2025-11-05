from Monitor import *

if __name__ == '__main__':
    monitor = Monitor("Samsung", 27, 150000, "Black")
    monitor.__str__()
    print('--' * 5, " 수정 ", '--' * 5)
    monitor.setCompany("LG")
    monitor.setInch(32)
    monitor.setPrice(300000)
    monitor.__str__()