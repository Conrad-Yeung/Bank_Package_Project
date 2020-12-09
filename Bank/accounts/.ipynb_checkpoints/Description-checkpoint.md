### ***Bank*** 
package contains the tools to create and manage banking features such as chequing accounts, saving accounts, credit cards and debit cards. The package is split into 2 subpackages.

### ***"accounts"*** subpackage:
Contains modules for initializing and managing bank accounts such as Chequings and Savings accounts. Contains 3 modules: "account" (baseclass),"chequing","saving". Each module contains class, for example in the "chequing" module, a class "Chequing" exists.

***How to use:***
1) Initialize the account: Create an object of the desired account type. Ex: ``` cheq = chequing("Conrad Yeung", initialdeposit = 10000) ```, will create a chequing account under the name Conrad Yeung with a balance of $10000.  
2) Use class methods to access various features. Ex: ```cheq.deposit(1000)```
3) If desired, direct attributes of the account can be accessed like any other object. Ex:```cheq.actype``` or ```cheq.bal```

***Cheat Sheet of attributes/features:***  
1) Attributes of both "Chequing" and "Saving" classes:
   * ```obj.name```: Account holder's name
   * ```obj.ac```: Account number
   * ```obj.bal```: Account balance
   * ```obj.bal_hist```: Account balance history (past 30)
   * ```obj.bal_time```: Times associated with transactions above.
   * ```obj.recent_transact```: Past 30 transactions (deposits and withdraws)
   * ```obj.trans_time```: Times associated with above.
   * ```obj.trans_lim```: Transaction limit (limit per withdraw)
   * ```obj.actype```: Type of account
  * Attributes unique to "Saving" class:
    * ```obj.intrate```: Interest rate 
    * ```obj.fixed_amount```: Amount in fixed deposit
    * ```obj.datestart```: Date fixed deposit started
    * ```obj.dateend```: Date fixed deposit will end
    * ```obj.fix_dep_inprocess```: If a fixed deposit is in process
2. Available functions to both "Chequing" and "Saving" classes
   * ```obj.details()```: Prints account details
   * ```obj.deposit(amount = 0)```: Deposit amount into account
   * ```obj.withdraw(amount=0)```: Withdraw amount from account
   * ```obj.summary()```: Shows account details and plot of the past 30 changes in your account balance.
   * ```obj.change_lim(newlim=self.trans_lim)```: Change the transaction limit of the account - will default to the value at the time of account creation (and by default is $1000)
 * Function unique to "Saving" class:
    * ```obj.setfixdeposit(amount=0,intrate=self.intrate,test=False)```: Create/Check a fixed depost for the account. The deposit will be locked in for a year and will automatically transfer the funds to your balance when the time period ends.