import folium
import pandas
data=pandas.read_csv("4.1 Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_producer(el):
    if elevation < 1000:
        return 'green'
    elif 100<=elevation<3000:
        return 'orange'
    else:
        return 'red' 

 #   return'green'
map=folium.Map(location=[38.58,-99.09],zoomstart=6,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")
for lt ,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lat,ln],radius=6 , popup=str(el)+"m",
    fill_color=color.producer(el),color="grey",fill_opacity=0.7
#color of the border of circle
#icon=folium.Icon(color_producer(el))))
# raduis for the circle shaped marker
fg.add_child(folium,GeoJson(data=(open('world.json','r',encoding='utf-8-sig'),
style_function=lambda x: {'fillcolor':'yellow'}))
map.add_child(fg)
map.save("Map1.html")
