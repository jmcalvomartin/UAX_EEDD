import streamlit as st
from PIL import Image


st.title("Mi primera web")
st.header("Autor: Jorge")

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
st.subheader("Logos de Python")
image = Image.open('/home/jorge/Documentos/GitHub/UAX_EEDD/Ejercicios/Web/images/logo1.png')
st.radio("Elegir Logo",("Logo1","Logo2"))
st.image(image)
