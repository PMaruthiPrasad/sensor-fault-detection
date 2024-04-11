class bank:
    def transactions(self):
        print('total transaction value' )
    
    def account_opening(self):
        print('this will show your account open status  ')

    def deposit(self):
        print('this will show your deposited amount' )  

class hdfc_bank(bank):
    def hdfc_to_icici(self):
        print('this will show you all the transactions from hdfc to icici' )    

class icici(hdfc_bank):
    pass

i=icici()
i.transactions()
i.deposit()
i.account_opening()
i.hdfc_to_icici()