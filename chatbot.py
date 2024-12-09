import os
import streamlit as st
import google.generativeai as genai

# Configuration de la clé API
os.environ["GEMINI_API_KEY"] = "AIzaSyBkmvajYfeNQnjv-UTy6k9o9ETyZgOdMOA"

# Fonction pour récupérer la réponse de Gemini
def get_gemini_response(prompt):
    try:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erreur lors de la génération de la réponse : {e}"

# Interface utilisateur Streamlit
st.markdown("""
<style>
body {
        background-image: url('assets/background.jpg');  /* Remplacez par l'image que vous voulez */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
.title {
    color: #3b82f6;
    font-size: 40px;
    font-weight: bold;
    text-align: center;
}
.input-container {
    background-color: #111827;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}
.input-text {
    background-color: #1f2937;
    border: none;
    color: #ffffff;
    font-size: 18px;
    border-radius: 8px;
    padding: 12px;
    width: 100%;
}
.button {
    background-color: #10b981;
    color: #ffffff;
    padding: 15px;
    border-radius: 8px;
    width: 100%;
    font-size: 18px;
    cursor: pointer;
    border: none;
    transition: all 0.3s ease;
}
.button:hover {
    background-color: #06b74c;
}
.response-container {
    background-color: #f3f4f6;
    border-radius: 12px;
    padding: 20px;
    margin-top: 20px;
    color: #111827;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}
.fade-in {
    animation: fadeIn 1s ease-in;
}
@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}
.image-container {
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Ajouter une image de logo ou d'icône
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image("assets/logo.jpg", width=200)  # Utiliser le fichier local logo.png
st.markdown('</div>', unsafe_allow_html=True)

# Titre
st.markdown('<h1 class="title">Chatbot Avancé avec Gemini</h1>', unsafe_allow_html=True)

# Message d'introduction
st.write("Posez une question, et notre chatbot intelligent vous répondra en quelques secondes !")

# Champ de texte pour entrer la question
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    prompt = st.text_area("Votre question :", key="input_text", help="Entrez votre question ici.", max_chars=300, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# Bouton pour générer la réponse
if st.button("Générer une Réponse", key="generate_button", use_container_width=True):
    if prompt:
        output = get_gemini_response(prompt)
        st.markdown('<div class="response-container fade-in">', unsafe_allow_html=True)
        st.write(f"**Réponse du Chatbot :**\n\n{output}")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.write("Veuillez entrer une question pour obtenir une réponse.")
