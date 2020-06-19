import folium
map=folium.Map(location=[38.58,-99.09],zoomstart=6,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.58,-99.09],popup="Hi aaku",icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map1.html")
