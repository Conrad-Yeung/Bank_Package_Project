# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import unittest
from testclass.asserttest_chq import Testchequing
#from testclass.accounting_savingtest import Testsaving

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(Testchequing))
#    suite.addTest(unittest.makeSuite(Testsaving))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
# -


