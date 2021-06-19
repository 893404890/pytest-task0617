from TESTcode.calulator import Calculator
class Test:
    def setup_class(self):
        self.c=Calculator()
        print('测试开始')
    def teardown_class(self):
        print('测试结束')
    def setup(self):
        print('start---------------')
    def teardown(self):
        print('end-----------------')
    def test_01(self):
        self.c=Calculator()

        assert 2== self.c.add(5.-3)
    def test_02(self):
        assert 3 == self.c.sub(9,4)