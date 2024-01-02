import streamlit as st
from model.generator import Generator, Model

def process_prompt(prompt, selected_model: Model):
    result = Generator(selected_model).generate(
        prompt=prompt
    )
    link_imagem = result[0]
    return link_imagem

def render_image(prompt):
    with col3:
        with st.spinner("Loading image..."):
            link_imagem = process_prompt(prompt, Model.get_value(selected_model))

    with col4:
            col2.image(link_imagem, caption="Result", use_column_width=True)

st.set_page_config(
    page_title="AI Image Generation",
    page_icon=":rocket:",
    layout="wide",
)

col1, col2 = st.columns([1, 1])

st.sidebar.header("Model Options")
model_options = Model.names()
selected_model = st.sidebar.radio("Select a Model", model_options)


col1.markdown("<h1 style='margin-bottom: 60px;'>AI Image Generation</h1>", unsafe_allow_html=True)

prompt = col1.text_area("Insert your prompt here", height=150, max_chars=500)

botao_processar = col1.button("Generate")

col3, col4 = st.columns(2)

st.markdown('<p style="color: #A9A9A9; font-weight: light;">Suggestions:</p>', unsafe_allow_html=True)

suggestions = [
    "A hyperrealistic portrait of a silver cyborg in the style of the “Mona Lisa”",
    "A pixelated 3D rendering of a skyscraper at midnight, dramatic lighting",
    "A picture of a robot wearing a clown suit, Unreal Engine"
]
sug1 = st.button(suggestions[0])
sug2 = st.button(suggestions[1])
sug3 = st.button(suggestions[2])

if sug1:
    render_image(prompt=suggestions[0])
if sug2:
    render_image(prompt=suggestions[1])
if sug3:
    render_image(prompt=suggestions[2])

if botao_processar:
    if not prompt.strip():
        col1.warning("Write something.")

    else:
        render_image(prompt=prompt)


st.caption("##### By Guilherme F. Sampaio")




