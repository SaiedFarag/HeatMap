import folium
from pyproj import crs
import geopandas as gpd
import matplotlib.pyplot as plt
import webbrowser
from folium.plugins import HeatMap

points_fp = r"K:\G\Python\HeatMap\addresses.shp"
points = gpd.read_file(points_fp)
# print(points.head())


m = folium.Map(location=[60.25, 24.8], zoom_start=10, control_scale=True, tiles='stamentoner')

folium.Marker(
    location=[60.20426, 24.96179],
    popup='Kumpula Campus',
    icon=folium.Icon(color='green', icon='ok-sign')
)

points_gjson = folium.features.GeoJson(points, name='Public transport stations')
# print(points_gjson.data.get('features'))
# Alternative syntax for adding points to the map instance
#m.add_child(points_gjson)
# points_gjson.add_to(m)

points['x'] = points['geometry'].x
points['y'] = points['geometry'].y

locations = list(zip(points['y'], points['x']))

HeatMap(locations, name='Heat Map').add_to(m)

folium.LayerControl().add_to(m)
m.save (r'K:\G\Python\New folder\example.html')
webbrowser.open(r'K:\G\Python\New folder\example.html')

# outfp = r'K:\G\Python\New folder\base_map.html'
# m.save(outfp)


# def auto_open(path):
#     html_page = f'{path}'
#     m.save(html_page)
#     # open in browser.
#     new = 2
#     webbrowser.open(html_page, new=new)