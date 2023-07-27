import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('example.xml')
root = tree.getroot()

# Reduce the price by $1 for books priced over $25
for book in root.findall('book'):
    price_element = book.find('price')
    price = float(price_element.text)
    if price > 25:
        price_element.text = str(price - 1)

# Add the "read" element with value "Yes" to the book "Data Science Basics"
for book in root.findall('book'):
    title_element = book.find('title')
    if title_element.text == 'Data Science Basics':
        read_element = ET.Element('read')
        read_element.text = 'Yes'
        book.append(read_element)

# Save the modified XML back to the file
tree.write('example_modified.xml')
