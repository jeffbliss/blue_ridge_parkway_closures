import requests, pprint
from bs4 import BeautifulSoup
from fastkml import kml

table_data = []
virginia_parkway_status = []
nc_parkway_status = []
url = 'https://www.nps.gov/blri/planyourvisit/roadclosures.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.findAll('table')

# this is true for now and is a big assumption
virginia_parkway_table = tables[1]
nc_parkway_table = tables[2]

# find all the rows in the table and throw it into table_data list
table_body = virginia_parkway_table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    table_data.append([ele for ele in cols if ele])

# create dictionary from table_data and push into parkway_status list
for row in table_data:
    if len(row) == 4:
        dict = {'mileposts': row[0], 'crossroads': row[1], 'status': row[2], 'notes': row[3]}
    else:
        dict = {'mileposts': row[0], 'crossroads': row[1], 'status': row[2]}
    virginia_parkway_status.append(dict)

# find all the rows in the table and throw it into table_data list
table_body = nc_parkway_table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    table_data.append([ele for ele in cols if ele])

# create dictionary from table_data and push into parkway_status list
for row in table_data:
    if len(row) == 4:
        dict = {'mileposts': row[0], 'crossroads': row[1], 'status': row[2], 'notes': row[3]}
    else:
        dict = {'mileposts': row[0], 'crossroads': row[1], 'status': row[2]}
    nc_parkway_status.append(dict)

pp = pprint.PrettyPrinter()
pp.pprint(virginia_parkway_status)
pp.pprint(nc_parkway_status)
    

#Read file into string and convert to UTF-8 (Python3 style)
#with open('doc.kml', 'rt') as myfile:
#    doc = myfile.read().encode('utf-8')

# Create the KML object to store the parsed result
#k = kml.KML()

# Read in the KML string
#k.from_string(doc)

# Get features
#features = list(k.features())
#placemarks_list = list(features[0].features())

#for placemark in placemarks_list:
#    print(placemark.extended_data.elements)

