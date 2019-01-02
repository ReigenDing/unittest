# -*- coding: utf-8 -*-

import unittest
from test_math import TestMathFunc


if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"),
             TestMathFunc("test_divide"), TestMathFunc('test_multi')]
    suite.addTests(tests)
    # with open('text.txt', 'a', encoding='utf-8') as fp:
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
