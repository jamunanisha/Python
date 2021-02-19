import os
import folium.plugins as plugins
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import webbrowser
from folium import plugins

df = pd.read_csv(r'C:\Users\User\Downloads\Ranipet parties.csv')
df.head()
df.shape

traffic_map = folium.Map(width=500, height=500, location=[13.1488, 80.2306], zoom_start=12)
Ranipet_json = os.path.join('https://raw.githubusercontent.com/tarunshah/India-D3/master/TamilNadu.geojson')
Ranipet_geojson = folium.GeoJson(Ranipet_json). add_to(traffic_map)
incidents = folium.map.FeatureGroup()
incidents = folium.map.FeatureGroup()
small_wildfires = folium.FeatureGroup(name='Green ADMK')
large_wildfires = folium.FeatureGroup(name='Red Dmk')
for i, v in df.iterrows():

    Colors = float(v['Colors'])

    popup = """
    Address : <b>%s</b><br>
    Parties: <b>%s</b><br>
    Colors:<b>%s</b><br>
    """ % (v['Address'], v['Colors'],
           v['Parties'],
           )
    if Colors in range(100, 550):
        folium.Marker(location=[v['Latitude'],
                                v['Longitude']],
                      popup='Custom Marker 1', tooltip='<strong>Click here to see Popup</strong>',
                      icon=folium.Icon(color='green', icon='none')).add_to(small_wildfires)
    if Colors in range(600, 1100):
        folium.Marker(location=[v['Latitude'],
                                v['Longitude']],
                      popup='Custom Marker 1', tooltip='<strong>Click here to see Popup</strong>',
                      icon=folium.Icon(color='red', icon='none')).add_to(large_wildfires)

small_wildfires.add_to(traffic_map)
large_wildfires.add_to(traffic_map)

folium.LayerControl(collapsed=False).add_to(traffic_map)
traffic_map
traffic_map.save('map.html')
