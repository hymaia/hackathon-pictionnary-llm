import base64
from io import BytesIO
from time import sleep

import streamlit as st
from PIL import Image
from src.game import Game
from src.send_data import DataGame
from streamlit_drawable_canvas import st_canvas

if 'game' not in st.session_state:
    st.session_state['game'] = Game()
    st.session_state['data_game'] = DataGame("toto")

game = st.session_state['game']
data_game: DataGame = st.session_state['data_game']


def send_image_to_chatgpt(image_data):
    # Convertir l'image numpy en image PIL
    image = Image.fromarray(image_data.astype('uint8'), 'RGBA')

    # Convertir l'image en bytes
    buffered = BytesIO()
    image.save(buffered, format="PNG")

    # Encoder l'image en base64
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Envoyer l'image encodée via la fonction send_image
    return game.evaluate_paint(img_str)

# Afficher le mot que le joueur doit dessiner
st.markdown(f"## Le mot à dessiner est : **{game.current_word()}**")

st.markdown(f'### Le dessin est : **{game.last_prediction}**')


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

col1, col2 = st.columns(2)
with col1:
    if st.button("Envoyer"):
        data_game.try_to_find(game.current_word())
        if canvas_result.image_data is not None:
            word = send_image_to_chatgpt(canvas_result.image_data)
            print("WORD -> ", word.lower())
            print("GAME -> ", game.current_word().lower())
            if (word.lower() in game.current_word().lower()) or (game.current_word().lower() in word.lower()):
                data_game.win_image(game.current_word())
                st.balloons()
                sleep(2)
                game.next_word()
            elif data_game.words_played[game.current_word()]["tries"] >= 10:
                data_game.fail_image(game.current_word())
                st.snow()
                sleep(2)
                game.next_word()
            st.rerun()
with col2:
    if st.button("Passer"):
        game.next_word()
        st.rerun()

