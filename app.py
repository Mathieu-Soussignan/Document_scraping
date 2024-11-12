import streamlit as st
import os

# Configuration de la page Streamlit
st.set_page_config(page_title="Lecteur de Documents Scraping", page_icon=":book:", layout="wide")

# Ajouter une image d'en-tête en point d'entrée sur la page principale
st.image("./assets/scraping_imdb.jpg", caption="L'art du scraping !", use_column_width=True)

# Liste des documents disponibles
documents_path = os.path.join(os.path.dirname(__file__), "data")

# Vérifiez si le chemin est correct
if not os.path.exists(documents_path):
    st.error(f"Le dossier '{documents_path}' n'existe pas. Vérifiez l'emplacement des fichiers.")
else:
    # Dictionnaire des fichiers à charger
    document_files = {
        "Scraping Book TP 1": os.path.join(documents_path, "scraping_book_tp_1.md"),
        "Scraping IMDb TP 2": os.path.join(documents_path, "scraping_imdb_tp_2.md")
    }

    # Barre latérale pour sélectionner le document
    st.sidebar.title("Sélectionner un document")
    selected_doc = st.sidebar.radio("Choisissez un document à afficher :", list(document_files.keys()))

    # Charger et afficher le document sélectionné
    file_path = document_files[selected_doc]

    # Vérification de l'existence du fichier
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                st.markdown(f"## {selected_doc}")
                st.markdown(content)
        except Exception as e:
            st.error(f"Erreur lors de la lecture du fichier : {e}")
    else:
        st.error(f"Le fichier '{file_path}' n'existe pas.")

# Section pour feedback utilisateur
st.sidebar.title("Feedback")
st.sidebar.text_area("Vos commentaires :")

# Pied de page
st.sidebar.markdown("Lecteur de documents conçu pour les récapitulatifs de TP.")