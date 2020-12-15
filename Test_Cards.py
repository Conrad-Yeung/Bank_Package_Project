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
from test_cards.test_cards_base import TestBaseCard
from test_cards.test_cards_credit import TestCreditCard
from test_cards.test_cards_debit import TestDebitCard

# Suite unit as explained in the lecture
def suite_cards():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestBaseCard))
    #suite.addTest(unittest.makeSuite(TestCreditCard))
    #suite.addTest(unittest.makeSuite(TestDebitCard))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
suite_cards()
# -


