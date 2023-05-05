import streamlit as st
from streamlit_folium import st_folium
import folium
from PIL import Image

st.set_page_config(
    page_title="Web Python UAX",
    page_icon="🧊",
    layout="wide",
    # expanded or collapsed
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.europeanvalley.es',
        'Report a bug': "https://www.europeanvalley.es",
        'About': "## Esto es una Web sobre documentación de **Python** \n ### UAX"
    })

st.sidebar.title("Menú")



col1,col2=st.columns(2)
col1.title("Mi primera web")
col1.header("Autor: Jorge")

image = Image.open('Ejercicios/Web/images/logo1.png')
col2.image(image, width=100)

st.divider()
st.markdown("### Asignatura: EEDD")
st.caption("Programación Python")

option=st.selectbox("Elige opción",("Funciones","Input"))

if option=="Funciones":
    code='''
    def prueba():
        for x in range (10):
            print("Test")
        return
    '''
else:
    code = '''
        num=input("Dime un número: )
        print(num)
        '''
st.code(code)

st.divider()
st.subheader("Datos de Python")
year=st.radio("Elegir Año",("Año 2000","Año 2023"))

if year=="Año 2000":
    st.metric(label="Ranking Mundial", value="4º", delta="-5º", delta_color="normal")
else:
    st.metric(label="Ranking Mundial", value="1º", delta="2º", delta_color="normal")

inf=st.checkbox("Información adicional", disabled=False)
if inf:
    contenedor=st.container()
    with contenedor:
        st.subheader("Definición")
        st.write("Esto es la definición de Python")

st.subheader("Versiones de Python")
tab1,tab2,tab3=st.tabs(["3.08","3.09","3.10"])

with tab1:
    st.write("Versión 3.08")

with tab2:
    st.write("Versión 3.09")

with tab3:
    st.write("Versión 3.10")

with st.expander("Referencias", expanded=False):
    st.write("Páginas oficiales de Python")

st.subheader("Mapa de programación")

if st.sidebar.button("Mapa"):
    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16, tooltip = "Liberty Bell")

    folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Test").add_to(m)

    st_folium(m, width=2000, height=500, returned_objects=[])