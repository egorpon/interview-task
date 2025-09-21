from bank_account import BankAccount, TransactionLog


class Bank:
    def __init__(self):
        self.bank_accounts = {}

    def __iter__(self):
        return iter(self.bank_accounts)

    def __getitem__(self, key):
        return self.bank_accounts[key]

    def __len__(self):
        return len(self.bank_accounts)

    def create_account(self, account_number, num=0):
        account = BankAccount(account_number, num)
        self.bank_accounts[account_number] = account
        return account

    def deposit_to_account(self, account_number, balance):
        acc = self.bank_accounts.get(account_number)
        acc.deposit(balance)

    def transfer_between_accounts(self, from_acc_num, to_acc_num, balance):
        from_acc = self.bank_accounts.get(from_acc_num)
        to_acc = self.bank_accounts.get(to_acc_num)
        from_acc.withdraw(balance)
        to_acc.deposit(balance)

    def get_total_balance(self):
        return sum(acc.balance for acc in self.bank_accounts.values())

    def get_richest_account(self):
        return max(self.bank_accounts.values(), key=lambda x: x.balance)


bank = Bank()
acc1 = bank.create_account("ACC001", 1000)
acc2 = bank.create_account("ACC002", 500)

bank.transfer_between_accounts("ACC001", "ACC002", 300)

for account in bank.bank_accounts:
    print(account)

print(f"Total balance: {bank.get_total_balance()}")
print(f"Richest account: {bank.get_richest_account()}")


for account in bank:
    print(account)

account = bank["ACC001"]
print(account)
print(f"Account balance: {account.balance}")

print(f"Number of accounts: {len(bank)}")
