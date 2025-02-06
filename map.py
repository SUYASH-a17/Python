import folium, pandas

data = pandas.read_csv('txt_fl/Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

# function for different colored markers based on elevation
def color_marker(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500<= elevation < 2500:
        return 'orange'
    else:
        return 'red'

# Create a map centered at a specific location
map = folium.Map(location=[40.76308734460247, -111.90743878552051], zoom_start=3)
folium.TileLayer(
    tiles='Stamen Terrain',
    attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>.' 
    'Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under ODbL.'
).add_to(map)

# create a feature group for markers
fgv = folium.FeatureGroup(name='Volcanoes')
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius= 7, popup=str(el)+" m", fill_color=color_marker(el), color='black', fill_opacity= 0.5))

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(
    data=open('txt_fl/world/world.json', 'r', encoding='utf-8-sig').read(),
    style_function =lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' 
                               if 10000000 <= x['properties']['POP2005'] < 50000000 else 'red'}
))

# add fg to the map
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# Save the map to an HTML file
map.save('map.html')
