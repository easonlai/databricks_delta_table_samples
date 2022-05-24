import pandas as pd
import json
import random

df = pd.read_csv('./to_json.csv')

for record in df.to_dict(orient='records'):
    json_file_name = './data/json/json' + str(random.randint(0, 100000000)) + '.json'
    with open(json_file_name, 'w') as file:
        to_json = json.dumps(record)
        file.write(to_json)