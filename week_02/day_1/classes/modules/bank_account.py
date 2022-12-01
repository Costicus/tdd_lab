class BankAccount: 
    def __init__(self, input_holder_name, input_balance, input_account_type):
        self.holder_name = input_holder_name
        self.balance = input_balance
        self.account_type = input_account_type
        self._rates = {
           "personal" : 10,
           "business" : 50 
        }

    def withdraw_money(self, amount):
        self.balance -= amount

    def pay_monthly_fee(self):
        self.balance -= self._rates[self.account_type]
    