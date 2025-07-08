# peta.py

import folium
import os
import geopandas

def tambah_layer_geojson(fg, geojson_path, nama_layer, warna_fill):
    style = {
        'color': 'black',
        'weight': 0.2,
        'fillColor': warna_fill,
        'fillOpacity': 0.25
    }
    fg.add_child(folium.GeoJson(
        geojson_path,
        name=nama_layer,
        style_function=lambda x: style
    ))

def peta_multi_layer():
    d = os.path.dirname(os.path.abspath(__file__))
    fg = folium.FeatureGroup(name="Semua Layer GeoJSON")

    # Daftar file geojson dan pengaturannya
    layers = [
        {"filename": "batuan_permukaan.json", "nama": "Batuan Permukaan", "warna": "blue"},
        {"filename": "Bulk_density.json", "nama": "Bulk density 2", "warna": "green"},
        {"filename": "C_org.json", "nama": "C organik 3", "warna": "red"},
        # Tambahkan lagi sesuai kebutuhan
    ]

    for layer in layers:
        geojson_path = os.path.join(d, layer["filename"])
        if not os.path.exists(geojson_path):
            # Jika file belum ada, bisa tambahkan proses konversi dari SHP ke GeoJSON di sini
            
            batuan_permukaan = geopandas.read_file(os.path.join(d, 'batuan_permukaan.shp'))
            batuan_permukaan.to_file(geojson_path, driver='GeoJSON')
            Bulk_density = geopandas.read_file(os.path.join(d, 'Bulk_density.shp'))
            Bulk_density.to_file(geojson_path, driver='GeoJSON')   
            C_org = geopandas.read_file(os.path.join(d, 'C_org.shp'))
            C_org.to_file(geojson_path, driver='GeoJSON')     
        if os.path.exists(geojson_path):
            tambah_layer_geojson(fg, geojson_path, layer["nama"], layer["warna"])

    return fg
