import base64
import random
from io import BytesIO
from time import sleep

import streamlit as st
from PIL import Image
from src.chatbot import generate_answer
from streamlit_drawable_canvas import st_canvas

word_list = ["maison", "voiture", "soleil", "arbre", "fleur", "montagne"]


def send_image_to_chatgpt(image_data):
    # Convertir l'image numpy en image PIL
    image = Image.fromarray(image_data.astype('uint8'), 'RGBA')

    # Convertir l'image en bytes
    buffered = BytesIO()
    image.save(buffered, format="PNG")

    # Encoder l'image en base64
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Envoyer l'image encodée via la fonction send_image
    return generate_answer(img_str)


# Champ de texte pour entrer le mot à dessiner
if 'word_to_draw' not in st.session_state:
    st.session_state["word_to_draw"] = random.choice(word_list)

# Afficher le mot que le joueur doit dessiner
st.markdown(f"## Le mot à dessiner est : **{st.session_state['word_to_draw']}**")


# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "point", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")


# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=True,
    height=600,
    width=600,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)


if st.button("Envoyer"):
    if canvas_result.image_data is not None:
        word = send_image_to_chatgpt(canvas_result.image_data)
        if (word.lower() in st.session_state['word_to_draw'].lower()) or (st.session_state['word_to_draw'].lower() in word.lower()):
            print("success")
            st.session_state['word_to_draw'] = random.choice(word_list)
            st.balloons()
            sleep(2)
            st.experimental_rerun()
