import json
from uuid import uuid4
data = json.load(open('database.json', mode='r'))

uid_index = dict()
category_index = dict()
for i, boxers_data in ['data_database']:
    boxers_data['uid'] = str(uuid4())
print(data)