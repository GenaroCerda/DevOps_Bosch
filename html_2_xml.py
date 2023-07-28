import csv

f = open('ut_results.csv')
csv_f = csv.reader(f)
data = []

for row in csv_f:
	data.append(row)
	
f.close()

print(data[1:])

def convert_row(row):
	return """<UNIT_TESTS_RESULTS>
	<TestCase>%s</TestCase>
	<Result>%s</Result>
</UNIT_TESTS_RESULTS>""" % (row[0], row[1])

with open ('output.xml', 'w') as f:
	f.write('\n'.join([convert_row(row) for row in data]))