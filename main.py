import jsonschema
from jsonschema import validate
from json import load


with open('schema.json') as f:
    schema = load(f)

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

list_ =[
    {'id': 1,'name':'anshik' ,'mobile': 950151651,'workPhone': 950151, 'DOB': 5-2-2002,'field': 'TU' },
    {'id': 2,'name':'harry' ,'workPhone': 950151, 'DOB': 5-2-1990,'field': 'TU' },
    {'id': 3,'name':'jason' ,'mobile': 950151651,'workPhone': 950151, 'govID': 1469,'field': 'MO' },
    {'id': 4,'name':'python' ,'mobile': 950151651,'homePhone': 950161, 'govID': 14659,'field': 'TU' },
    {'id': 5,'name':'java' ,'workPhone': 950151, 'govID': 15669,'field': 'SU' }
]

isValid = validateJson(list_)

if isValid:
   print("True")
else:
    print("False")