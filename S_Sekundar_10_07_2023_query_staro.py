import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('S_Sekundar_10_07_2023.xml')
root = tree.getroot()

# Add the "Vazi_do" element with value "2015-06-28T00:00:00+01:00" to the all Dijagnoza with ID_dijagnoza in data set {Z00, Z01, Z03, Z000, Z001, Z008, Z016, Z017, Z018, Z019, Z038, Z039} "
for dijagnoza in root.findall('Dijagnoza'):
    idDijagnoza_element = dijagnoza.find('ID_dijagnoza')
    if idDijagnoza_element.text == 'Z00' or idDijagnoza_element.text == 'Z01' or idDijagnoza_element.text == 'Z03' or idDijagnoza_element.text == 'Z000' or idDijagnoza_element.text == 'Z001' or idDijagnoza_element.text == 'Z008' or idDijagnoza_element.text == 'Z016' or idDijagnoza_element.text == 'Z017' or idDijagnoza_element.text == 'Z018' or idDijagnoza_element.text == 'Z019' or idDijagnoza_element.text == 'Z038' or idDijagnoza_element.text == 'Z039':
        vaziDo_element = ET.Element('Vazi_do')
        vaziDo_element.text = '2015-06-28T00:00:00+01:00'
        dijagnoza.append(vaziDo_element)

# Save the modified XML back to the file
tree.write('S_Sekundar_10_07_2023_bezXmlns.xml')
