import csv
import pandas as pd

results = []
with open('ut_result.log', 'r') as input_file:
    with open('ut_result.csv', 'w') as output_file:
        line_count = 0
        for line in input_file:
            if line_count == 0:
                writer = csv.writer(output_file)
                writer.writerow(['TestCase', 'Result'])
                line_count = line_count + 1
            else:
                if line.startswith('test_'):
                    rows = line.split(' ')
                    writer.writerow(rows[0:2])
                   
df1 = pd.read_csv('ut_result.csv')
html_string = df1.to_html()
print(html_string)