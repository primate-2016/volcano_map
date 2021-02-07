import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elevation = list(data['ELEV'])
volcano = list(data['NAME'])

# create some html to use for the popups on the map
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# create a map object, tiles is the base map format to use
map = folium.Map(zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="mymap")

# create a pointer on the map for each volcano
for lt, ln, vlc, el in zip(lat, lon, volcano, elevation):
    # create an iframe containing the html above and the volcano name etc.
    iframe = folium.IFrame(html=html % (vlc, vlc, el), width=200, height=100)
    # add each volcano as a point to the feature group for the map
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))

# add all the points to the map
map.add_child(fg)

map.save("volcanos.html")