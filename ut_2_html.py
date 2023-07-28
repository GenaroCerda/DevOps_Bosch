import csv

results = []
with open('ut_results.log', 'r') as input_file:
    with open('ut_results.csv', 'w') as output_file:    
        for line in input_file:
            if line.startswith('test_'):
                rows = line.split(' ')
                writer = csv.writer(output_file)
                writer.writerow(rows[0:2])
