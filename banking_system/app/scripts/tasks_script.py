from app.models import Account, Customer, Transaction

def task_1_basic():
    """
    Отримати:
    1. Всі активні рахунки (is_active=True)
    2. Всіх VIP клієнтів  
    3. Рахунки з балансом більше 10000
    4. Ощадні рахунки (savings) VIP клієнтів
    """
    
    # 1. Активні рахунки
    active_accounts = Account.objects.filter(is_active=True)
    
    # 2. VIP клієнти
    vip_customers = Customer.objects.filter(is_vip=True)
    
    # 3. Рахунки з великим балансом
    rich_accounts = Account.objects.filter(balance__gt=10000)
    
    # 4. Ощадні рахунки VIP клієнтів
    vip_savings = Account.objects.filter(account_type='savings',customer__is_vip=True)
    
    return active_accounts, vip_customers, rich_accounts, vip_savings


# Завдання 2: Агрегація
def task_2_aggregation():
    """
    Порахувати:
    1. Загальну суму балансів всіх рахунків
    2. Кількість транзакцій для кожного рахунку (annotate)
    3. Середній баланс для кожного типу рахунку
    """
    from django.db.models import Sum, Count, Avg, Q
    
    # 1. Сума всіх балансів
    total_balance = Account.objects.aggregate(total_balance=Sum('balance'))
    
    # 2. Рахунки з кількістю транзакцій
    accounts_with_count = Account.objects.annotate(amount_of_transactions=Count('transactions')).values('id', "amount_of_transactions")
    
    # 3. Середній баланс по типах
    avg_by_type = Account.objects.aggregate(avg_savings = Avg('balance', filter=Q(account_type='savings')), avg_checking = Avg('balance', filter=Q(account_type='checking')))
    
    return total_balance, accounts_with_count, avg_by_type


# Завдання 3: Складніші запити
def task_3_complex():
    """
    Знайти:
    1. Клієнтів, які мають 2 або більше рахунків
    2. Топ-3 клієнти за сумарним балансом всіх їх рахунків
    3. Рахунки без жодної транзакції
    """
    from django.db.models import Sum, Count
    
    # 1. Клієнти з багатьма рахунками
    customers_multiple_accounts = Customer.objects.annotate(total_accounts = Count('accounts')).filter(total_accounts__gte=2)
    
    # 2. Топ-3 найбагатші клієнти  
    top_customers = Customer.objects.annotate(total_balance = Sum('accounts__balance')).order_by('-total_balance')[:3].values('user__username','total_balance')    
    # 3. Рахунки без транзакцій
    accounts_no_transactions = Account.objects.annotate(amount_of_transactions=Count('transactions')).filter(amount_of_transactions=0)
    
    return customers_multiple_accounts, top_customers, accounts_no_transactions

def run():
    for i in task_1_basic():
        print(i)
    
    for i in task_2_aggregation():
        print(i)

    for i in task_3_complex():
        print(i)

