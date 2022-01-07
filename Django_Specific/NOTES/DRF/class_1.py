# API
# REST

# Install DRF
# pip install djangorestframework

# project/setting.py
import json
Installed_APPS = [
    '....',
    'rest_framework',
]

"""
Python has a built in package called json, which is used to work with json data.

dumps(data) - This is used to convert python object into json string.

loads(data) - This is used to parse json string to python objects
ex :-
"""

python_data = {'name': 'Anagh', 'roll': 101}
json_data = json.dumps(python_data)
print(json_data)  # {"name":"Anagh","roll",101}

parsed_data = json.loads(json_data)
print(parsed_data)  # {'name':'Anagh','roll',101}
