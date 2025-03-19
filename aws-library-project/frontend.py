import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("📖 Bibliothèque en ligne")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["🔍 Rechercher un livre", "➕ Ajouter un livre", "📥 Emprunter un livre", "👤 Gérer utilisateurs"])

# Rechercher un livre
if menu == "🔍 Rechercher un livre":
    st.header("🔍 Rechercher un livre")
    search_query = st.text_input("Entrez le titre du livre")
    if st.button("Rechercher"):
        response = requests.get(f"{API_URL}/books/", params={"title": search_query})
        if response.status_code == 200:
            books = response.json()
            if books:
                st.table(pd.DataFrame(books))
            else:
                st.warning("Aucun livre trouvé.")
        else:
            st.error("Erreur lors de la recherche.")

# Ajouter un livre
elif menu == "➕ Ajouter un livre":
    st.header("➕ Ajouter un livre")
    title = st.text_input("Titre du livre")
    author = st.text_input("Auteur")
    if st.button("Ajouter"):
        if title and author:
            response = requests.post(f"{API_URL}/books/", json={"title": title, "author": author})
            if response.status_code == 200:
                st.success(f"📚 Livre '{title}' ajouté avec succès !")
            else:
                st.error("Erreur lors de l'ajout du livre.")
        else:
            st.warning("Veuillez remplir tous les champs.")

# Emprunter un livre
elif menu == "📥 Emprunter un livre":
    st.header("📥 Emprunter un livre")
    book_title = st.text_input("Titre du livre à emprunter")
    if st.button("Emprunter"):
        response = requests.post(f"{API_URL}/borrow/", params={"title": book_title})
        if response.status_code == 200:
            st.success(f"✅ Livre '{book_title}' emprunté avec succès !")
        else:
            st.warning("Livre non disponible ou inexistant.")

# Gérer utilisateurs
elif menu == "👤 Gérer utilisateurs":
    st.header("👤 Gérer les utilisateurs")
    user_name = st.text_input("Nom de l'utilisateur")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ajouter utilisateur"):
            if user_name:
                response = requests.post(f"{API_URL}/users/", json={"name": user_name})
                if response.status_code == 200:
                    st.success(f"👤 Utilisateur '{user_name}' ajouté avec succès !")
                else:
                    st.warning("L'utilisateur existe déjà.")
            else:
                st.warning("Veuillez entrer un nom.")

    with col2:
        if st.button("Supprimer utilisateur"):
            if user_name:
                response = requests.delete(f"{API_URL}/users/", params={"name": user_name})
                if response.status_code == 200:
                    st.success(f"🗑️ Utilisateur '{user_name}' supprimé.")
                else:
                    st.warning("Utilisateur introuvable.")
            else:
                st.warning("Veuillez entrer un nom.")