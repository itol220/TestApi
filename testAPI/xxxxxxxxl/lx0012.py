import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class demotest(unittest.TestCase):
    def setup(self):
        print ("this is the setup")

    @data(2,3)
    def testb(self,value):
        print (value)
        print ("this is test b")

    @data([2,3],[4,5])
    def testa(self,value):
        print (value)
        print ("this is test a")

    @data([2, 3], [4, 5])
    @unpack
    def testc(self, first,second):
        print (first)
        print (second)
        print ("this is test c")

    @file_data('d:/data_dic.json')
    def test_dic(self,value):
        print (value)
        print ('this is dic')

    @file_data('d:/Data.yml')
    def test_yml(self, value):
        print (value)
        print ('this is yml')

    def teardown(self):
        print ("this is the down")

if __name__ == '__main__':
    unittest.main()
    #suite=unittest.TestLoader.getTestCaseNames(demotest)
    #suite = unittest.TestLoader().loadTestsFromTestCase(demotest)
    #unittest.TextTestRunner(verbosity=2).run(suite)