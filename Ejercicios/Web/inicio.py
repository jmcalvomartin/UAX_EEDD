#Entorno Web
import streamlit as st
from PIL import Image

#Configurar la página
st.set_page_config(
    page_title="Web de Python",
    page_icon="😜",
    initial_sidebar_state="collapsed" #expanded
)
logo=Image.open("Ejercicios/Web/images/logopython.png")

st.sidebar.image(logo,width=60)
st.sidebar.title("Menú")
help=st.sidebar.checkbox("Ayuda", disabled=False)

col1,col2=st.columns(2)

with col1:
    st.title("Web de Python")
    st.header("UAX")
    st.write("Autor: Jorge")

with col2:
    st.image(logo,width=70)


st.divider() #Linea

st.caption("Ejemplos de código")

option=st.selectbox("Elija un ejemplo",("Funciones","Input"))
if option=="Funciones":
    code='''
    def prueba():
        for x in range (10):
            print("Test")
        return
        '''
else:
    code = '''
       num1=input("Dime un número")
       print(num1)
           '''
st.code(code)

st.divider()
st.caption("Datos de Python")
year=st.radio("Elegir Año",("Año 2000","Año 2023"))
if year=="Año 2000":
    st.metric(label="Ranking Mundial", value="4º", delta="-3º")
if year=="Año 2023":
    st.metric(label="Ranking Mundial", value="1º", delta="2º")

st.divider()

cont1=st.container()

if st.sidebar.button("Mostrar Versiones"):
    with cont1:
        st.header("Versiones de Python")
        tab1,tab2,tab3=st.tabs(["3.08","3.09","3.10"])
        with tab1:
            st.write("La versión 3.08 de Python")
        with tab2:
            st.write("La versión 3.09 de Python")
        with tab3:
            st.write("La versión 3.10 de Python")
if st.sidebar.button("Ocultar Versiones"):
        with cont1:
            st.write("")

if help==True:
    st.sidebar.header("Descripción de Python")
    st.sidebar.write("Python es un lenguaje de alto nivel")