# def __init__(self, input_holder_name, input_balance, input_account_type):
#         self.holder_name = input_holder_name
#         self.balance = input_balance
#         self.account_type = input_account_type

class Student:
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort

    def talk(self):
        return ("I can talk!")

    def say_favourite_language(self, language):
        return ("I love " + language)

# from modules.bank_account import *

# bank_account = BankAccount("John", 10, "personal")
# bank_account_2 = BankAccount("Greg", 100, "business")

