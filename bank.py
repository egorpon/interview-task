from bank_account import BankAccount


class Bank:
    def __init__(self):
        self.bank_accounts = set()

    def create_account(self, account_number, num=0):
        account = BankAccount(account_number, num)
        self.bank_accounts.add(account)
        return account

    def deposit_to_account(self, account_number, amount):
        for acc in self.bank_accounts:
            if acc.account_number == account_number:
                acc.deposit(amount)

    def transfer_between_accounts(self, from_acc_num, to_acc_num, amount):
        for acc in self.bank_accounts:
            from_acc = acc.account_number == from_acc_num
            to_acc = acc.account_number == to_acc_num
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            


bank = Bank()
acc1 = bank.create_account("ACC001", 1000)
acc2 = bank.create_account("ACC002", 500)

bank.transfer_between_accounts("ACC001", "ACC002", 300)

for account in bank.bank_accounts:
    print(account)
