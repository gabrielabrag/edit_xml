import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

for year in root.iter('year'):
    new_year = int(2023)
    year.text = str(new_year)

tree.write('output2.xml')