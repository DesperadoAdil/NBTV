import os
from app import app
import unittest



if __name__ == '__main__':
    testdir = "app/test/"
    discover = unittest.defaultTestLoader.discover(testdir, pattern='test_*.py')
    runner=unittest.TextTestRunner()
    runner.run(discover)
    unittest.main()