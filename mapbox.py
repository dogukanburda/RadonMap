import pandas as pd
import streamlit as st
import altair as alt
from streamlit_folium import folium_static
import folium

st.title("Maps for Visualizing Radon Activity")
st.write("""
Radon is a naturally
occuring noble gas originated from radioactive decay series of 238U,235U.
""")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


coordinates = [[41.106730, 29.024172],[41.104514, 29.024371],[41.104927591058654, 29.026060320686536]]
def make_map(tile_type):
    main_map = folium.Map(location=(41.106730, 29.024172), zoom_start=14,tiles=tile_type)
    tooltip = "Detector #"
    i=1
    for lat,lng in coordinates:
        desc=f"<b>Coordinates:</b>{lat,lng}\n <b>Current Activity:</b>: 4 pCi"
        folium.CircleMarker(location=[lat,lng],
                        tooltip=desc,
                        fill=True,
                        #fill_color=,
                        color=None,
                        fill_opacity=0.5,
                        radius=10,
                        popup = '<b>'+tooltip+str(1)+'</b>'+ '  ' + desc
                        ).add_to(main_map)
        i+=1
    return main_map








options = st.multiselect(
     'Dedektör Seçiniz',
     ['Dedektör #1', 'Dedektör #2','Dedektör #3','Dedektör #4','Dedektör #5','Dedektör #6','Dedektör #7'],
     ['Dedektör #1', 'Dedektör #2','Dedektör #3','Dedektör #4','Dedektör #5','Dedektör #6','Dedektör #7'])

#st.write('You selected:', options)



# metric_for_map = st.selectbox('Dedektör Seçiniz',
#                               options=['Dedektör #1','Dedektör #2'],
#                               index=0)
main_map = make_map('Stamen Toner')

folium_static(main_map)
main_map = make_map('OpenStreet Map')

folium_static(main_map)


main_map = make_map('Stamen Terrain')

folium_static(main_map)


main_map = make_map('cartodbpositron')

folium_static(main_map)









coordinates = [ [29.024172,41.106730],[29.024371,41.104514],[29.026060320686536,41.104927591058654]]
#coordinates = [[41.106730, 29.024172],[41.104514, 29.024371],[41.104927591058654, 29.026060320686536]]
map_data = pd.DataFrame(coordinates,columns=['lon', 'lat'])
st.write(map_data)
st.map(map_data,zoom=14)