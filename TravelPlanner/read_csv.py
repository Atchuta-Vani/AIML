def read_csv_file(csv_file_name):
    import csv
    f = open(csv_file_name, 'r')
    csv_reader = csv.DictReader(f)
    itinerary = []
    for row in csv_reader:
        #print(row)
        itinerary.append(row)
    f.close()
    return itinerary;