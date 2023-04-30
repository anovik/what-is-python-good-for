import xmltodict
import json
from zipfile import ZipFile

with open("output.xml") as xml_file:         
    parsedDict = xmltodict.parse(xml_file.read(), attr_prefix='', cdata_key='text')    
    
json = json.dumps(parsedDict, indent=1)     

with open("output.json", "w") as json_file:
    json_file.write(json)       
    
with ZipFile('output.zip', 'w') as zipFile:
    zipFile.write('output.json')