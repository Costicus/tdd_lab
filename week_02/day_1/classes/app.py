from modules.bank_account import *

bank_account = BankAccount("John", 10, "personal")
bank_account_2 = BankAccount("Greg", 100, "business")

bank_account.pay_monthly_fee()
bank_account_2.pay_monthly_fee()

print(bank_account.balance)
print(bank_account_2.balance)

# print(bank_account.holder_name)
# bank_account.holder_name = "Dave"
# print(bank_account.holder_name)


account = {
    "holder_name": "John",
    "balance": 500,
    "type": "business"
}

