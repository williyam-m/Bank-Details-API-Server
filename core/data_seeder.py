from .models import Bank, Branch
import csv


csv_file = 'dataset/bank_branches.csv'

with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bank, created = Bank.objects.get_or_create(name=row['bank_name'])


        branch = Branch.objects.create(
                    ifsc=row['ifsc'],
                    bank=bank,
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state'],
        )

print("Data seeding completed!")