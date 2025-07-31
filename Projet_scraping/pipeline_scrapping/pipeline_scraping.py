# pipeline_scraping.py

import sys
import os
# Ajoute le dossier parent (Projet_scraping) 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importation des fonctions nécessaires depuis les autres modules
from get_data.get_scraping_data import scrape_books
from process_data.process_scrapping_data import clean_scraped_data
from database.insert_data import insert_books_to_db
import pandas as pd

def run_scraping_pipeline():
    print("Début du pipeline de scraping")

    # 1. Scraper les données depuis le site
    print("Étape 1 : Scraping des données...")
    df_raw = scrape_books()
    print(f"{len(df_raw)} livres scrapés")

    # 2. Sauvegarder les données brutes dans un fichier CSV
    print("Étape 2 : Sauvegarde des données brutes...")
    df_raw.to_csv("data/data_scraping.csv", index=False)
    print("Données brutes sauvegardées dans 'data/data_scraping.csv'")

    # 3. Nettoyer les données
    print("Étape 3 : Nettoyage des données...")
    df_cleaned = clean_scraped_data(df_raw)
    print("Données nettoyées")

    # 4. Insérer les données dans la base de données
    print("Étape 4 : Insertion en base de données...")
    insert_books_to_db(df_cleaned)
    print("Données insérées en base")

    print("Pipeline terminé avec succès !")
