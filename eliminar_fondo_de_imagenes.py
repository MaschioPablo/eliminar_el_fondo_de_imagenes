

import streamlit as st
from PIL import Image
from rembg import remove
import io
import os

#todo BACK-END
#todo //FUNCIONES
def procesar_imagen (image_upload):
    image = Image.open(image_upload)
    imagen_procesada = eliminar_fondo(image)
    return imagen_procesada

def eliminar_fondo (image):
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    imagen_procesada_por_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(imagen_procesada_por_bytes))

#todo FRONT-END
st.image("lamborghini_green.JPG")
st.image("lamborghini_png.PNG")
st.header("Background Removal App")
st.subheader("Upload an image")
uploaded_image = st.file_uploader ("choose an image..", type=("jpg", "jpeg", "png"))

if uploaded_image is not None:
    st.image(uploaded_image, caption="imagen subida", use_column_width=True)
    
    remove_button = st.button(label="eliminar fondo")
    if remove_button:
        imagen_procesada_final = procesar_imagen(uploaded_image)
        
        st.image(imagen_procesada_final, caption="fondo eliminado", use_column_width=True)
        
        imagen_procesada_final.save("imagen procesada.png")
        
        with open("imagen procesada.png", "rb") as f:
            image_data = f.read()
        st.download_button("descargar imagen", data=image_data, file_name="imagen_procesada.png")
        
        os.remove("imagen procesada.png")
        
