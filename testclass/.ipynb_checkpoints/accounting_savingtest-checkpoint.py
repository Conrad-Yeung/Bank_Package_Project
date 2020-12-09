import unittest
from datetime import datetime


import Bank.accounts.account as acct
import Bank.accounts.chequing as ch
import Bank.accounts.saving as sv

class Testsaving (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.sav1 = sv.Saving("Conrad Yeung")
        cls.sav2 = sv.Saving("Aamir Khan",0,1500)
        print("Class created")
        
    @classmethod
    def tearDownClass(cls):
        print("Class torn down")
    
    def setUp(self):
        print("\tStart Test")
        
    def tearDown(self):
        print("\tTest Complete\n")
    
    def test_1deposit(self):
        print("Testing saving.deposit")
        #Should deposit sucesfully
        self.sav1.deposit(102.69)
        self.sav2.deposit(1500)
        self.assertEqual(self.sav1.bal,102.69)
        self.assertEqual(self.sav2.bal,1500)
        #Should not deposit sucuessfully: Due to value < 0 (balance will be the balance above)
        self.sav1.deposit(-100)
        self.sav2.deposit(-0.001)
        self.assertEqual(self.sav1.bal,102.69)
        self.assertEqual(self.sav2.bal,1500)
        
    def test_2withdraw(self):
        print("Testing saving.withdraw")
        #Should withdraw sucesfully
        self.sav1.withdraw(69)
        self.sav2.withdraw(29.90)
        self.assertEqual(self.sav1.bal,102.69-69)
        self.assertEqual(self.sav2.bal,1500-29.90)
        #Should not withdraw sucesfully: Due to value < 0 (balance will be the balance above)
        self.sav1.withdraw(-1)
        self.sav2.withdraw(-0.00000123123)
        self.assertEqual(self.sav1.bal,102.69-69)
        self.assertEqual(self.sav2.bal,1500-29.90)
        #Should not withdraw sucesfully: Due to value > Transaction Limit (balance will be the balance above)
        self.sav1.withdraw(1500.1)
        self.sav2.withdraw(3001)
        self.assertEqual(self.sav1.bal,102.69-69)
        self.assertEqual(self.sav2.bal,1500-29.90)
    
    def test_3change_lim(self):
        print("Testing saving.change_lim")
        #Default limits are sucessfull
        self.assertEqual(self.sav1.trans_lim,1000)
        self.assertEqual(self.sav2.trans_lim,1500)
        #Changes limit sucessfully
        self.sav1.change_lim(500)
        self.sav2.change_lim(2000)
        self.assertEqual(self.sav1.trans_lim,500)
        self.assertEqual(self.sav2.trans_lim,2000)
        self.sav1.withdraw(0.69)
        self.sav2.withdraw(21)
        self.assertEqual(self.sav1.bal,33.69-0.69)
        self.assertEqual(self.sav2.bal,1470.1-21)   
        #Change limit failed
        self.sav1.change_lim(-1)       
        self.assertEqual(self.sav1.trans_lim,500)
        
    def test_4setfixdeposit(self):
        print("Testing saving.setfixdeposit")
        date_today = datetime(datetime.today().year,datetime.today().month,datetime.today().day)
        date_next_year = datetime(datetime.today().year+1,datetime.today().month,datetime.today().day)
        #Creating Fix Deposit & Checking Values (Deposit amount, Interest Rate, Date locked in and Date end)
        self.sav1.setfixdeposit(1000)
        self.sav2.setfixdeposit(500,0.5)
        self.assertEqual([self.sav1.fixed_amount,self.sav1.intrate,self.sav1.datestart,self.sav1.dateend,self.sav1.fix_dep_inprocess], [1000,0.01,date_today,date_next_year,1])
        self.assertEqual([self.sav2.fixed_amount,self.sav2.intrate,self.sav2.datestart,self.sav2.dateend,self.sav2.fix_dep_inprocess], [500,0.5,date_today,date_next_year,1])
        #Should fail - Trying to Create a Fix deposit while active 
        self.sav1.setfixdeposit(1000)
        self.sav2.setfixdeposit(500,0.5)
        self.assertEqual([self.sav1.fixed_amount,self.sav1.intrate,self.sav1.datestart,self.sav1.dateend,self.sav1.fix_dep_inprocess], [1000,0.01,date_today,date_next_year,1])
        self.assertEqual([self.sav2.fixed_amount,self.sav2.intrate,self.sav2.datestart,self.sav2.dateend,self.sav2.fix_dep_inprocess], [500,0.5,date_today,date_next_year,1])
        #Despoit into bal & reset fixed desposit - When fixed deposit date is reached
        self.sav1.setfixdeposit(1000,0.1,True)
        self.sav2.setfixdeposit(500,0.5,True)
        self.assertEqual([self.sav1.fixed_amount,self.sav1.intrate,self.sav1.datestart,self.sav1.dateend,self.sav1.fix_dep_inprocess], [1000,0.01,0,0,0])
        self.assertEqual([self.sav2.fixed_amount,self.sav2.intrate,self.sav2.datestart,self.sav2.dateend,self.sav2.fix_dep_inprocess], [500,0.5,0,0,0])
        self.assertEqual(self.sav1.bal,33+(1000+1000*0.01))
        self.assertEqual(self.sav2.bal,1449.1+(500+500*0.5))
        
    def test_5balance_history_attribute(self):
        print("Testing saving.bal_hist and .bal_time")
        #Check Sucessfull balance history changes
        self.assertEqual(self.sav1.bal_hist,[0,102.69,102.69-69,102.69-69-0.69,33+(1000+1000*0.01)])
        self.assertEqual(self.sav2.bal_hist,[0,1500,1500-29.90,1500-29.90-21,1449.1+(500+500*0.5)])                    
        #Check the number of Time entries match number of balance changes (Since Times will be essentially the same)
        self.assertEqual(len(self.sav1.bal_hist),len(self.sav1.bal_time))
        self.assertEqual(len(self.sav2.bal_hist),len(self.sav2.bal_time))


