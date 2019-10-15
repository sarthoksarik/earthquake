import json

eq_raw_data_file = 'data/eq_data_1_day_m1.json'

with open(eq_raw_data_file) as df:
    readable_eq_data = json.load(df)
readable_eq_file = 'data/readable_eq_data_ss.json'

with open(readable_eq_file, 'w') as rdf:
    json.dump(readable_eq_data, rdf, indent=4, separators=('ppp', 'jjj'))

all_eq_data = readable_eq_data['features']

print(len(all_eq_data))
