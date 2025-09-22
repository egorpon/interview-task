from app.models import Customer, Account, Transaction, User
from faker import Faker
import random
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(5):
            User.objects.create_user(username=fake.user_name(), password="test")

        users = User.objects.all()

        for user in random.sample(list(users), 5):
            Customer.objects.get_or_create(
                user=user, is_vip=random.choice([True, False])
            )

        customers = Customer.objects.all()

        for customer in random.sample(list(customers), 5):
            Account.objects.create(
                account_number=fake.iban(),
                customer=customer,
                account_type=random.choice(["savings", "checking"]),
                balance=fake.random_int(min=5000, max=20000),
                is_active=random.choice([True, False]),
            )

        accounts = Account.objects.all()
        for _ in range(10):
            for acc in random.sample(list(accounts),1):
                Transaction.objects.create(account=acc,amount=fake.random_int(min=10,max=999),transaction_type=random.choice(['withdraw','deposit','transfer']))