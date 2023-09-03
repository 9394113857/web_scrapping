# Import the necessary libraries
import csv

# Load the saved scrapped data from the CSV file
data_rows = []
with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader) # Read the first row as headers
    for row in reader:
        data_rows.append(row)

# Print the headers
print(','.join(headers))

# Print all the data rows
for i, data_row in enumerate(data_rows, 1):
    print(f"{i}. {','.join(data_row)}")





