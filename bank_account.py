import datetime


class WithdrawException(Exception):
    pass


class TransactionLog:
    def __repr__(self):
        return (
            f"Time: {self.time}; Type: {self.transaction_type}; Amount: {self.amount}"
        )

    def __init__(self, transaction_type, amount):
        self.time = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount


class BankAccount:
    def __repr__(self):
        return f"Your account number is {self.account_number}, your balance is {self.amount}"

    def __init__(self, account_number, amount=0):
        self.account_number = account_number
        self.amount = amount
        self.__transaction_history = []

    def log(self, type_of_operation, num):
        trasaction = TransactionLog(type_of_operation, num)
        self.__transaction_history.append(trasaction)

    def deposit(self, num):
        self.amount += num
        self.log("deposit", num)

    def withdraw(self, num):
        if self.amount < num:
            raise WithdrawException("You don't have much money")
        self.amount -= num
        self.log("withdraw", num)

    def get_transaction_history(self):
        return self.__transaction_history

    @property
    def current_amount(self):
        return self.amount
