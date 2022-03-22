import pandas as pd
import numpy as np
import plotly.express as px
df1 = pd.read_csv('data/kc_house_data.csv')
df1['date'] = pd.to_datetime(df1['date'])
print('oi')
data_map = df1[['id', 'lat', 'long', 'price']]
street_map = px.scatter_mapbox(data_map, 
                               lat ='lat', 
                               lon = 'long', 
                               hover_name = 'id' , 
                               hover_data = ['price'], 
                               color_discrete_sequence = ['fuchsia', 'red'], 
                               zoom = 3, 
                               height=300)

street_map.update_layout(mapbox_style = 'open-street-map')
street_map.update_layout(height = 600, margin = {'r':0, 't':0, 'l':0, 'b':0})
street_map.show()