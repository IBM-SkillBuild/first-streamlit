import streamlit as st 
import requests
from PIL import Image

# para coger emojies
# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Streamlit Edu", page_icon=":partying_face:",layout="wide")


url = "https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/15665/production/_107435678_perro1.jpg"
img = Image.open(requests.get(url, stream=True).raw)
img.save('img1.jpg')
st.sidebar.markdown("My first Streamlit Proyect")
st.sidebar.image("./capucha.png")
boton_html="""<button style="width:auto;height:30px">boton html</buttom>"""
with st.container():
  columna_derecha,columna_izquierda=st.columns([1,2])
  with columna_derecha:
      
      st.markdown(boton_html,unsafe_allow_html=True)
      st.subheader("prueba de subheader")
      st.title("prueba de titulo")
      imagen=columna_derecha.file_uploader("carga una imagen")
  with columna_izquierda:   
    
    st.markdown(" # prueba titulo markdown")
    st.write("prueba simple st.write('xxxxx')")
    st.write("[ir a la foto del perro ](https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/15665/production/_107435678_perro1.jpg)")
    if imagen:
      st.image(imagen)
    columna_izquierda.camera_input("dsdsd")  



