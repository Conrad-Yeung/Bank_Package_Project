import unittest
from datetime import datetime

import Bank.accounts.account as acct
import Bank.accounts.chequing as ch
import Bank.accounts.saving as sv

class Testchequing (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.cheq1 = ch.Chequing("Conrad Yeung", 1500)
        cls.cheq2 = ch.Chequing("Aamir Khan", 2000,3000)
        print("Class created")
        
    @classmethod
    def tearDownClass(cls):
        print("Class torn down")
        print("#################")
    
    def setUp(self):
        print("\tStart Test")
        
    def tearDown(self):
        print("\tTest Complete\n")
    
    def test_1deposit(self):
        print("Testing chequing.deposit")
        #Should deposit sucesfully
        self.cheq1.deposit(1000.52)
        self.cheq2.deposit(100)
        self.assertEqual(self.cheq1.bal,1500+1000.52)
        self.assertEqual(self.cheq2.bal,2000+100)
        #Should not deposit sucuessfully: Due to value < 0 (balance will be the balance above)
        self.cheq1.deposit(-100)
        self.cheq2.deposit(-0.001)
        self.assertEqual(self.cheq1.bal,1500+1000.52)
        self.assertEqual(self.cheq2.bal,2000+100)
        
    def test_2withdraw(self):
        print("Testing chequing.withdraw")
        #Should withdraw sucesfully
        self.cheq1.withdraw(569)
        self.cheq2.withdraw(29.90)
        self.assertEqual(self.cheq1.bal,2500.52-569)
        self.assertEqual(self.cheq2.bal,2100-29.90)
        #Should not withdraw sucesfully: Due to value < 0 (balance will be the balance above)
        self.cheq1.withdraw(-1)
        self.cheq2.withdraw(-0.00000123123)
        self.assertEqual(self.cheq1.bal,2500.52-569)
        self.assertEqual(self.cheq2.bal,2100-29.90)
        #Should not withdraw sucesfully: Due to value > Transaction Limit (balance will be the balance above)
        self.cheq1.withdraw(1500.1)
        self.cheq2.withdraw(3001)
        self.assertEqual(self.cheq1.bal,2500.52-569)
        self.assertEqual(self.cheq2.bal,2100-29.90)
    
    def test_3change_lim(self):
        print("Testing chequing.change_lim")
        #Default limits are sucessfull
        self.assertEqual(self.cheq1.trans_lim,1000)
        self.assertEqual(self.cheq2.trans_lim,3000)
        #Changes limit sucessfully
        self.cheq1.change_lim(1400)
        self.cheq2.change_lim(20)
        self.assertEqual(self.cheq1.trans_lim,1400)
        self.assertEqual(self.cheq2.trans_lim,20)
        self.cheq1.withdraw(1400)
        self.cheq2.withdraw(21)
        self.assertEqual(self.cheq1.bal,1931.52-1400)
        self.assertEqual(self.cheq2.bal,2070.1)   
        #Change limit failed
        self.cheq1.change_lim(-1400)       
        self.assertEqual(self.cheq1.trans_lim,1400)
        
    def test_4balance_history_attribute(self):
        print("Testing chequing.bal_hist and .bal_time")
        #Check Sucessfull balance history changes
        self.assertEqual(self.cheq1.bal_hist,[1500,1500+1000.52,2500.52-569,1931.52-1400])
        self.assertEqual(self.cheq2.bal_hist,[2000,2000+100,2100-29.90])                    
        #Check the number of Time entries match number of balance changes (Since Times will be essentially the same)
        self.assertEqual(len(self.cheq1.bal_hist),len(self.cheq1.bal_time))
        self.assertEqual(len(self.cheq2.bal_hist),len(self.cheq2.bal_time))

