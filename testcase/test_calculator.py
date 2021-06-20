import pytest
import yaml

from TESTcode.calulator import Calculator
def getdata():
    with open('../testdata/calculator.yaml') as f:
        t=yaml.safe_load(f)
        return (t['data1'],t['ids1'],t['data2'],t['ids2'],t['data3'],t['ids3'],t['data4'],t['ids4'])
print(getdata())
class Test:

    def setup_class(self):
        self.c=Calculator()
        print('测试开始')
    def teardown_class(self):
        print('测试结束')
    def setup(self):
        print('开始计算')
    def teardown(self):
        print('结束计算')
    @pytest.mark.parametrize('a,b,expect',getdata()[0],ids=getdata()[1])
    @pytest.mark.add
    def test_add(self,a,b,expect):

        assert expect == self.c.add(a,b)

    @pytest.mark.parametrize('a,b,expect',getdata()[2],ids=getdata()[3])
    @pytest.mark.sub
    def test_sub(self,a,b,expect):

        assert expect == self.c.sub(a,b)

    @pytest.mark.parametrize('a,b,expect', getdata()[4], ids=getdata()[5])
    @pytest.mark.mul
    def test_mul(self, a, b, expect):
            assert expect == self.c.multiplication(a, b)


    @pytest.mark.parametrize('a,b,expect', getdata()[6], ids=getdata()[7])
    @pytest.mark.div
    def test_mul(self, a, b, expect):
         try:

            assert expect == self.c.div(a, b)
         except:

            assert expect == 'divisor cannot be 0'
