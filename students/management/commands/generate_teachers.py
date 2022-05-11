from django.core.management.base import BaseCommand
from students.models import Teachers
from faker import Faker


class Command(BaseCommand):
    help = 'Generates random teachers vase on input amount'

    def add_arguments(self, parser):
        parser.add_argument('numbers_of_teachers', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        fake = Faker()
        result = []

        for i in range(options['numbers_of_teachers']):
            result.append(Teachers(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.pyint(1, 100),
                seniority=fake.pyint(1, 30)
            ))
        Teachers.objects.bulk_create(result)

        self.stdout.write(self.style.SUCCESS('Successfully created teachers'))
