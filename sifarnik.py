import zipfile
import glob
import os
import xml.etree.ElementTree as ET

file_path = glob.glob('S_Sekundar_*.xml')[0]
file_path_poz = glob.glob('Pozicija_Sekundar_*.xml')[0]

output_zip_file = os.path.splitext(os.path.basename(file_path))[0] + '.zip'
output_zip_file_poz = os.path.splitext(os.path.basename(file_path_poz))[0] + '.zip'

replacements = {
  '<?xml version="1.0" standalone="yes"?>\n': '',
  ' xmlns="http://tempuri.org/dstSifarnici.xsd"': ''
}

def find_replace(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


find_replace(file_path, replacements)

# Parse the XML file
tree = ET.parse(file_path)
root = tree.getroot()

zabranjene_dijagnoze = ['Z00', 'Z01', 'Z03', 'Z000', 'Z001', 'Z008', 'Z016', 'Z017', 'Z018', 'Z019', 'Z038', 'Z039']

# Add the "Vazi_do" element with value "2015-06-28T00:00:00+01:00" to the all Dijagnoza with ID_dijagnoza in data set {Z00, Z01, Z03, Z000, Z001, Z008, Z016, Z017, Z018, Z019, Z038, Z039} "
for dijagnoza in root.findall('Dijagnoza'):
    idDijagnoza_element = dijagnoza.find('ID_dijagnoza')
    if idDijagnoza_element.text in zabranjene_dijagnoze:
        vaziDo_element = ET.Element('Vazi_do')
        vaziDo_element.text = '2015-06-28T00:00:00+01:00'
        dijagnoza.append(vaziDo_element)

# Save the modified XML back to the file
tree.write(file_path)

# Vratiti zaglavlje XML fajla kakvo je bilo
replacement_nazad = {
  '<dstSifarnici': '<?xml version="1.0" standalone="yes"?>\n<dstSifarnici xmlns="http://tempuri.org/dstSifarnici.xsd"'
}

# Vraćanje zaglavlja
find_replace(file_path, replacement_nazad)

with zipfile.ZipFile(output_zip_file, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
    zipf.write(file_path, arcname=file_path)
    
with zipfile.ZipFile(output_zip_file_poz, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
    zipf.write(file_path_poz, arcname=file_path_poz)
