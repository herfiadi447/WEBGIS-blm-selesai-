from flask import Flask, render_template
import folium
from peta2 import peta_multi_layer
from basemap2 import basemaps1

app = Flask(__name__)

@app.route('/')
def index():
    # Peta untuk dashboard
    dashboard_map = folium.Map(location=[-4.47, 119.61], zoom_start=12, control_scale=True)
    basemaps = basemaps1()
    for layer in basemaps.values():
        layer.add_to(dashboard_map)
    peta_multi_layer(dashboard_map)
    folium.LayerControl().add_to(dashboard_map)
    dashboard_map_html = dashboard_map._repr_html_()

    # Peta untuk geo-ai (bisa layer berbeda, atau sama)
    geoai_map = folium.Map(location=[-4.47, 119.61], zoom_start=12, control_scale=True)
    basemaps = basemaps1()
    for layer in basemaps.values():
        layer.add_to(geoai_map)
    peta_multi_layer(geoai_map)
    folium.LayerControl().add_to(geoai_map)
    geoai_map_html = geoai_map._repr_html_()

    return render_template(
        'index.html',
        dashboard_map_html=dashboard_map_html,
        geoai_map_html=geoai_map_html
    )

if __name__ == '__main__':
    app.run(debug=True)
