import datetime


class WithdrawException(Exception):
    pass


class TransactionLog:
    def __repr__(self):
        return (
            f"TransactionLog(time={self.time}, transaction_type={self.transaction_type}, balance={self.balance}"
        )

    def __init__(self, transaction_type, balance):
        self.time = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.balance = balance


class BankAccount:
    def __repr__(self):
        return f"Account: {self.account_number}"

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.__transaction_history = []

    def log(self, type_of_operation, num):
        trasaction = TransactionLog(type_of_operation, num)
        self.__transaction_history.append(trasaction)

    def deposit(self, num):
        self.balance += num
        self.log("deposit", num)

    def withdraw(self, num):
        if self.balance < num:
            raise WithdrawException("You don't have much money")
        self.balance -= num
        self.log("withdraw", num)

    def get_transaction_history(self):
        return self.__transaction_history

    @property
    def current_amount(self):
        return self.balance
