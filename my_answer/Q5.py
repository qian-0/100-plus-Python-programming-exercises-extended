class IoString(object):
    s = ''
    def __init__(self, str_):
        self.s = str_
    def toUp(self):
        self.s = self.s.upper()
    def show(self):
        print(self.s)

if __name__ == '__main__':
    str_ = input("请输入一个大小写字符串：")
    s = IoString(str_)
    s.toUp()
    s.show()
