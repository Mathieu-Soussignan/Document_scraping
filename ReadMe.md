# Lecteur de Documents Scraping

Bienvenue dans l'application **Lecteur de Documents Scraping**, une application Streamlit qui permet de lire et de consulter des documents relatifs au scraping de données. Cette application est conçue pour être facile à utiliser et permet d'accéder rapidement aux différents documents disponibles, ainsi qu'à une application de scraping externe.

## Fonctionnalités

- **Lecture de documents** : Sélectionnez un document dans la barre latérale pour afficher son contenu. Les documents disponibles incluent des tutoriels sur le scraping de données.
- **Image d'en-tête** : Une image est affichée en page principale pour un accueil visuel attrayant.
- **Lien vers une application de scraping externe** : Un lien est disponible dans la barre latérale pour accéder à une autre application Streamlit dédiée au scraping.
- **Feedback utilisateur** : La barre latérale permet aux utilisateurs de laisser des commentaires pour améliorer l'application.

## Prérequis

- **Python 3.7+**
- **Streamlit** : Vous devez installer la bibliothèque Streamlit pour exécuter cette application.

## Installation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone <url_du_dépôt>
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd LecteurDeDocumentsScraping
   ```

3. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application Streamlit :
   ```bash
   streamlit run app.py
   ```

2. Ouvrez votre navigateur à l'adresse indiquée par Streamlit (par défaut : [http://localhost:8501](http://localhost:8501)).

3. Utilisez la barre latérale pour sélectionner les documents disponibles et accéder aux fonctionnalités.

## Organisation du Projet

- **app.py** : Fichier principal de l'application.
- **assets/** : Contient les images utilisées dans l'application, telles que l'image d'en-tête et l'icône de l'application de scraping.
- **data/** : Dossier contenant les fichiers markdown des documents de TP sur le scraping.

## Fonctionnalités supplémentaires

- **Lien vers l'application de scraping** : Un lien visuel est intégré dans la barre latérale pour accéder à une application Streamlit externe dédiée au scraping.
- **Commentaire utilisateur** : Les utilisateurs peuvent donner des commentaires via une section dédiée dans la barre latérale.

## Contribuer

Les contributions sont les bienvenues. Pour proposer des améliorations :

1. Forkez le projet.
2. Créez une nouvelle branche pour vos modifications :
   ```bash
   git checkout -b feature/ma-nouvelle-fonctionnalité
   ```
3. Commitez vos modifications :
   ```bash
   git commit -m "Ajout de ma nouvelle fonctionnalité"
   ```
4. Pushez sur la branche :
   ```bash
   git push origin feature/ma-nouvelle-fonctionnalité
   ```
5. Créez une Pull Request.

## Licence

Ce projet est sous licence MIT.

## Auteur

Développé par [Mathieu Soussignan](https://www.mathieu-soussignan.com).
