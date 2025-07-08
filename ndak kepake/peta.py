from flask import Flask
import folium
import os
from flask import render_template
import geopandas
app = Flask(__name__)

@app.route('/')
def peta1():
    d = os.path.dirname(os.path.abspath(__file__))
    batuan_permukaan = geopandas.read_file(d+'/batuan_permukaan.shp')
    batuan_permukaan.to_file(d+'/batuan_permukaan.json', driver='GeoJSON')

    map = folium.Map(location=[-4.47, 119.61], zoom_start = 11)

    batuan_permukaan_border = {
        'color': 'black',
        'weight': 0.2,
        'fillcolor' : 'blue',
        'fillOpacity': 0.25
    }

    data = os.path.join(d+'/batuan_permukaan.json')
    folium.GeoJson(data, name="Batuan_Permukaan", style_function = lambda x:batuan_permukaan_border).add_to(map)

    return map._repr_html_()
if __name__== '__main__':
    app.run(debug=True)