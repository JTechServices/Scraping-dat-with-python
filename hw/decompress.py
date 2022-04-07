from zipfile import ZipFile

with ZipFile('astra_export_xml .zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('xml')