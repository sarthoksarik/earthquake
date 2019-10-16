import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

eq_raw_data_file = r'data\eq_data_30_day_m1.json'

with open(eq_raw_data_file) as df:
    readable_eq_data = json.load(df)
readable_eq_file = 'data/readable_eq_data_ss.json'

with open(readable_eq_file, 'w') as rdf:
    json.dump(readable_eq_data, rdf, indent=4)

all_eq_data = readable_eq_data['features']

prop_list = (mags, lons, lats) = ([], [], [])

for eq_data in all_eq_data:
    mag = eq_data['properties']['mag']
    lon = eq_data['geometry']['coordinates'][0]
    lat = eq_data['geometry']['coordinates'][1]
    prop_values = (mag, lon, lat)
    for props, vals in zip(prop_list, prop_values):
        props.append(vals)

# print(f"magnitudes: {mags[:5]}")
# print(f"longitudes: {lons[:5]}")
# print(f"lattitudes: {lats[:5]}")

# map the earthquakes

eq_data = [{'type': 'scattergeo',
            'lon': lons,
            'lat': lats,
            'marker': {
                'size': [mag**2 for mag in mags],
                'color': mags,
                'colorscale': 'Viridis',
                'reversescale': True,
                'colorbar':{'title': 'Magnitude', },
            },
            }]
eq_layout = Layout(title='Global Earthquakes')

eq_wm_fig = {'data': eq_data, 'layout': eq_layout}
offline.plot(eq_wm_fig, filename='onedayeq.html')
