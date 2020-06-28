import csv

input_file = 'input.csv'
output_file = 'output.csv'

# -----------------------------------------------------------------------------
# Reading with csv.reader()
# -----------------------------------------------------------------------------
with open(input_file, 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')

    # (Optionally) skip the header row
    next(csv_data)

    for line in csv_data:
        #print(line)
        print(line[1])

# -----------------------------------------------------------------------------
# Writing with csv.writer()
# -----------------------------------------------------------------------------
with open(input_file, 'r') as csv_file:
    csv_data = csv.reader(csv_file)

    with open(output_file, 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_data:
            csv_writer.writerow(line)

# -----------------------------------------------------------------------------
# Reading with csv.DictReader()
# -----------------------------------------------------------------------------
with open(input_file, 'r') as csv_file:
    csv_data = csv.DictReader(csv_file)

    for line in csv_data:
        # print(line)
        print(line['Symbol'])

# -----------------------------------------------------------------------------
# Writing with csv.DictWriter()
# -----------------------------------------------------------------------------
with open(input_file, 'r') as csv_file:
    csv_data = csv.DictReader(csv_file)

    with open(output_file, 'w') as new_file:
        
        # fieldNames = ['Symbol', 'Name', 'Last', 'Sector', 'Yield', 'Score']
        fieldNames = ['Symbol', 'Last', 'Sector', 'Yield', 'Score'] # then del 'Name' from writerow() below

        csv_writer = csv.DictWriter(new_file, fieldnames = fieldNames, delimiter=';')

        csv_writer.writeheader()

        for line in csv_data:
            del line['Name']
            csv_writer.writerow(line)