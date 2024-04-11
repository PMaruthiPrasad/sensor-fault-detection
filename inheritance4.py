class bank:
    def transactions(self):
        print('total transaction value' )
    
    def account_opening(self):
        print('this will show your account open status  ')

    def deposit(self):
        print('this will show your deposited amount' )  
    def test(self):
        print("this is test method from bank")

class hdfc_bank:
    def hdfc_to_icici(self):
        print('this will show you all the transactions from hdfc to icici' )   
    def test(self):
        print("this is test method from hdfc bank")

class ineuron_bank:
    def account_status_icici(self):
        print("print a account status in icici bank")
class icici(bank,hdfc_bank,ineuron_bank):
    pass
i=icici()
i.transactions()
i.account_opening()
i.deposit()
i.hdfc_to_icici()
i.test()
i.account_status_icici()
