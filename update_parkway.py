import requests, pprint
from bs4 import BeautifulSoup
from fastkml import kml

pp = pprint.PrettyPrinter()

#### CONSTANTS
style_constants_dict = {
    'line_closed': '#line-A52714-4100',
    'line_open': '#line-558B2F-4100',
    'line_ungated': '#line-7CB342-4294',
    'icon_open': '#icon-1739-558B2F',
    'icon_closed': '#icon-1739-A52714'
}




################################ SCRAPING PARKWAY OPEN/CLOSED STATUS
table_data = []
parkway_status = []
url = 'https://www.nps.gov/blri/planyourvisit/roadclosures.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.findAll('table')

# this is true for now and is a big assumption
virginia_parkway_table = tables[1]
nc_parkway_table = tables[2]

# find all the rows in the virginia table and throw it into table_data list
table_body = virginia_parkway_table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    table_data.append([ele for ele in cols if ele])

# find all the rows in the nc table and throw it into table_data list
table_body = nc_parkway_table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    table_data.append([ele for ele in cols if ele])

# create dictionary from table_data and push into parkway_status list
for row in table_data:
    mileposts = row[0]
    # remove all newlines and & from crossroads
    crossroads = row[1].replace("\n", " ")
    crossroads = crossroads.replace("&", "and")
    # Remove all asterisks from Ungated*
    status = row[2].replace("*", "")
    if len(row) == 4:
        notes = row[3]
        dict = {'mileposts': mileposts, 'crossroads': crossroads, 'status': status, 'notes': notes}
    else:
        dict = {'mileposts': mileposts, 'crossroads': crossroads, 'status': status}
    parkway_status.append(dict)




################################ READING KML FILE AND MODIFYING IT WITH NEW STATUS
kml_file = 'modified_name.kml'
with open(kml_file, 'rt') as myfile:
    doc=myfile.read().encode('utf-8')

k=kml.KML()
k.from_string(doc)

features = list(k.features())
features_list = list(features[0].features())

""" Two foor loops to go through the parkway_status dict and the kml file Placemarks
    compare names and then break out of inner for loop if there is a match.
    There are currently a handful of non matches that need to be added to the kml file.
    For every match, update the description, styleUrl, and extended data status and notes"""
for placemark in features_list:
    match = False
    mileposts = None
    crossroads = None
    status = None
    notes = None
    styleUrl = 'line'

    if (placemark.styleUrl.split('-')[0] == '#icon'): # check if style is line or icon
        styleUrl = 'icon'
    
    for row in parkway_status:
        if match == True:
            break
        mileposts = row['mileposts']
        crossroads = row['crossroads']
        status = row['status']
        notes = 'No Notes'
        if len(row) == 4:
            notes = row['notes']
        if placemark.name == crossroads:
            match = True
   
    if match == True:
        placemark.description = f'Mileposts: {mileposts}<br>Status: {status}<br>Notes: {notes}'

        # probably a better way to do this style line silliness
        if styleUrl == 'line' and status == 'Open':
            placemark.styleUrl = style_constants_dict['line_open']
        elif styleUrl == 'line' and status == 'Closed':
            placemark.styleUrl = style_constants_dict['line_closed']
        elif styleUrl == 'line' and (status == 'Ungated' or status == 'Ungated*'):
            placemark.styleUrl = style_constants_dict['line_ungated']
        elif styleUrl == 'icon' and status == 'Open':
            placemark.styleUrl = style_constants_dict['icon_open']
        else: # assume icon style of closed
            placemark.styleUrl = style_constants_dict['icon_closed']

        for element in placemark.extended_data.elements:
            if element.name == 'status':
                element.value = status
            elif element.name == 'notes':
                element.value = notes
       
with open("output.kml", "wt") as f:
    f.writelines(k.to_string(prettyprint=True))
