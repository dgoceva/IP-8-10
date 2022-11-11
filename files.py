import json
import csv
import pandas

with open('lorem.txt') as f:
    print(f.read())

with open('lorem.txt') as f:
    for line in f:
        print(line.upper())

f = open('lorem.txt', 'a')
f.write('Vestibulum eleifend in purus quis gravida. Donec eget sagittis ipsum. Vestibulum pellentesque pharetra ultrices. Integer et ornare ligula, in porta libero. Suspendisse vehicula consectetur erat, in euismod nibh tincidunt nec. Nam lobortis, lacus at fringilla tincidunt, nisi metus sagittis felis, vitae vehicula turpis ligula a velit. Proin non velit elementum massa scelerisque lobortis sit amet id arcu. In vel pellentesque elit.')
f.close()

with open('lorem.txt') as f:
    print(f.readlines())

with open('euro_countries.json') as f:
    countries = json.load(f)

# print(type(countries), countries)

result = []
for country in countries:
    if country['name'].startswith(('B', 'E')):
        result.append(country)
with open('countries.json', 'w') as f:
    json.dump(result, f)

with open('euro_coutries.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'code'])
    writer.writeheader()
    for country in countries:
        writer.writerow(country)

with open('countries.csv') as f:
    reader = csv.DictReader(f)
    for country in reader:
        print(country)

data = pandas.read_csv('countries.csv')
print(data)
