import datetime
import csv

monthly_reports = {}
with open('transactions.csv', newline='') as csvfile:
	transactions_reader = csv.DictReader(csvfile)
	for row in transactions_reader:
		post_datetime = datetime.datetime.strptime(row['posted_at'], '%Y-%m-%dT%H:%M:%S.%f%z')

		year_month = datetime.datetime.strftime(post_datetime, "%Y %B")
		if year_month not in monthly_reports :
			monthly_reports[year_month] = []
		
		monthly_reports[year_month].append(
			row
		)

print(f'YYYY <month> -- in      out     ')
for month, transactions in monthly_reports.items() :
	month_credit_total = 0.0
	month_deposit_total = 0.0
	for tr in transactions :
		if tr['transaction_type'] == 'Credit' :
			month_credit_total += float(tr['amount'])
		else :
			month_deposit_total += float(tr['amount'])

	print(f'{month:12s} -- {month_credit_total:7.2f} {month_deposit_total:7.2f}')
