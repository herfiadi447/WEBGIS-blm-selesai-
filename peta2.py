# peta.py

import folium
import os
import geopandas

def tambah_layer_geojson(map_obj, geojson_path, nama_layer, tooltip_fields):
    def style_function(feature):
        props = feature['properties']
        # Tentukan warna berdasarkan tingkat kesesuaian
        if props.get('S1_BP', 0) == 1:
            fillColor = '#1a9641'  # hijau tua (Sangat Sesuai)
        elif props.get('S2_BP', 0) == 1:
            fillColor = '#a6d96a'  # hijau muda (Cukup Sesuai)
        elif props.get('S3_BP', 0) == 1:
            fillColor = '#fdae61'  # oranye (Marginal Sesuai)
        elif props.get('N_BP', 0) == 1:
            fillColor = '#d7191c'  # merah (Tidak Sesuai)
        else:
            fillColor = '#cccccc'  # abu-abu (tidak diketahui)
        return {
            'color': 'black',
            'weight': 0.2,
            'fillColor': fillColor,
            'fillOpacity': 0.5
        }
    fg = folium.FeatureGroup(name=nama_layer)
    fg.add_child(folium.GeoJson(
        geojson_path,
        name=nama_layer,
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=tooltip_fields)
    ))
    map_obj.add_child(fg)

def peta_multi_layer(map_obj):
    d = os.path.dirname(os.path.abspath(__file__))
    layers = [
        {
            "filename": "batuan_permukaan.json",
            "nama": "Batuan Permukaan",
            "warna": "blue",
            "fields": ['BATUAN_NIL', 'S1_BP', 'S2_BP', 'S3_BP', 'N_BP']
        },
        {
            "filename": "KTK.json",
            "nama": "KTK 2",
            "warna": "green",
            "fields": ['KTK_NILAI', 'S1_KTK', 'S2_KTK', 'S3_KTK', 'N_KTK']
        },
        {
            "filename": "C_org.json",
            "nama": "C organik 3",
            "warna": "red",
            "fields": ['C_org_NILAI', 'S1_C_org', 'S2_C_org', 'S3_C_org', 'N_C_org']
        },
    ]
    for layer in layers:
        geojson_path = os.path.join(d, layer["filename"])
        if not os.path.exists(geojson_path):
            shp_path = geojson_path.replace('.json', '.shp')
            if os.path.exists(shp_path):
                gdf = geopandas.read_file(shp_path)
                gdf.to_file(geojson_path, driver='GeoJSON')
        if os.path.exists(geojson_path):
            tambah_layer_geojson(map_obj, geojson_path, layer["nama"], layer["fields"])
