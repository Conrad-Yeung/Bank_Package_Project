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
from datetime import datetime

import Bank.accounts.saving as sv

class Testchequing (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Initialize the account I will actually use for testing - create a history of 30 deposits (0 deposits)
        cls.ac1 = sv.Saving("Conrad Yeung", 1500)
        for i in range(0,29):
            cls.ac1.deposit(0)
        cls.ac2 = sv.Saving("Aamir Khan",1000)
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test0_createclass(self):
        #Try again - creation failed
        me=sv.Saving(123,123)
        me=sv.Saving("C2A3W",123)
        me=sv.Saving("Conrad","awd")
        me=sv.Saving("Conrad",-69)
        me=sv.Saving("Conrad",69,"awd")
        me=sv.Saving("Conrad",69,-1)
        #Sucessfull
        me=sv.Saving("Conrad",1000,2500)
        self.assertEqual(me.name,"Conrad")
        self.assertEqual(me.bal,1000)
        self.assertEqual(me.bal_hist,[1000])
        self.assertEqual(len(me.bal_time),1)
        self.assertEqual(me.recent_transact,[])
        self.assertEqual(me.trans_time,[])
        self.assertEqual(me.trans_lim,2500)
        self.assertEqual(me.actype,"Chequings")
        
    def test_1deposit(self):
        #Try again - deposit failed
        self.ac1.deposit(-12)
        self.ac1.deposit("meow")
        #Deposit Sucessful 
        self.ac1.deposit(500)
        self.ac2.deposit(1000)
        self.assertEqual(self.ac1.bal,1500+500)
        self.assertEqual(sum(self.ac1.bal_hist),1500*29+2000)
        self.assertEqual(len(self.ac1.bal_time),30)
        self.assertEqual(sum(self.ac1.recent_transact),500)
        self.assertEqual(len(self.ac1.trans_time),30)
        
        self.assertEqual(self.ac2.bal,1000+1000)
        self.assertEqual(sum(self.ac2.bal_hist),1000+(1000+1000))
        self.assertEqual(len(self.ac2.bal_time),2)
        self.assertEqual(sum(self.ac2.recent_transact),1000)
        self.assertEqual(len(self.ac2.trans_time),1)
        
    def test_2withdraw(self):
        #Try again - deposit failed
        self.ac1.withdraw(-1231)
        self.ac1.withdraw("BARK")
        self.ac1.withdraw(1500)
        #Deposit Sucessful 
        self.ac1.withdraw(250)
        self.ac2.withdraw(20)
        self.assertEqual(self.ac1.bal,1500+500-250)
        self.assertEqual(sum(self.ac1.bal_hist),(1500*28)+2000+(2000-250))
        self.assertEqual(len(self.ac1.bal_time),30)
        self.assertEqual(sum(self.ac1.recent_transact),500-250)
        self.assertEqual(len(self.ac1.trans_time),30)
        
        self.assertEqual(self.ac2.bal,1000+1000-20)
        self.assertEqual(sum(self.ac2.bal_hist),1000+(1000+1000)+(2000-20))
        self.assertEqual(len(self.ac2.bal_time),2+1)
        self.assertEqual(sum(self.ac2.recent_transact),1000-20)
        self.assertEqual(len(self.ac2.trans_time),1+1)
        
    def test_3change_lim(self):
        #Change limit failed
        self.ac1.change_lim(-1)       
        self.ac1.change_lim("MOO")
        #Default limits are sucessfull
        self.assertEqual(self.ac1.trans_lim,1000)
        #Changes limit sucessfully
        self.ac1.change_lim(500)
        self.assertEqual(self.ac1.trans_lim,500)
        self.ac1.change_lim(2000)
        self.assertEqual(self.ac1.trans_lim,2000)
        self.ac1.change_lim(2000)
        self.assertEqual(self.ac1.trans_lim,2000)
        
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
        
    def test_5details_summ(self):
        self.ac1.details()
        self.ac1.summary()
        self.ac2.details()
        self.ac2.summary()

