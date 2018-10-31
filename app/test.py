import os
from app import app
import unittest


testdir = "app/test/"
discover = unittest.defaultTestLoader.discover(testdir, pattern='test_*.py')
runner=unittest.TextTestRunner()
runner.run(discover)
unittest.main()