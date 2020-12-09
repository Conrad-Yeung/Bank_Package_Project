# Data-533-Lab-2

Group: Aamir Khan and Conrad Yeung  
Package: Bank  
Sub-packages: Accounts and Transactions

1) Account modules:  
a) Base Account class:  
        i) Deposit  
        ii) Withdraw  
        iii) Summary  
b) Savings (inherits Base) class:  
        i) Inherits – Deposit, Withdraw, Summary  
        ii) Set Max Withdrawal for Savings  
        iii) Interest Rate (show interest rate)  
c) Chequings (inherits Base) class:  
        i) Inherits – Deposit, Withdraw, Summary
        ii) Set Max Withdrawal for Chequings
        
2) Cards modules:  
a) Card class:  
i) Pay  
ii) Summary  
b) Credit Card (inherits Card) class:  
i) Inherits – Pay and Summary  
ii) Set Credit Limit  
iii) Check Credit Limit  
c) Debit Card (inherit Card) class:  
i) Inherits – Pay and Summary  
ii) Type of Card  
iii) Check Transaction Limit  

Functions:
1)	Deposit:  Money goes into account
2)	Withdraw: Money leaves account  
a)	Pay – Money leaves account
3)	Summary: Balance, Past 10 transactions
4)	Set Max …: Max withdrawal amount per transaction
a)	Set Credit/Transaction Limit: Max withdrawal amount per transaction
5)	Interest Rate – Show current interest rate
6)	Type of Card: Debit Card Details (Type of Card, Max Transaction Limit, Owner Name)

