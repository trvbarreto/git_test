import unittest
import main


class TestMain(unittest.TestCase):
    # Execute before each function
    def setUp(self):
        print('🚀🚀🚀 about to test a function')

    def test_do_stuff(self):
        '''TEST ONE'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asda'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    # Execute after each function
    def tearDown(self):
        print('🧹🧹🧹 Cleaning up')


if __name__ == '__main__':
    unittest.main()
