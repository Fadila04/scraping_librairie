
# process_scrapping_data.py

import pandas as pd

# Dictionnaire pour convertir les ratings en chiffres
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# Fonction de nettoyage des données scrapées
def clean_scraped_data(df):
    df = df.copy()  # Bonne pratique pour éviter de modifier l'original

    # Nettoyer les prix : enlever le symbole £ et convertir en float
    df["price"] = df["price"].str.replace("Â", "").str.replace("£", "").astype(float)

    # Nettoyer la disponibilité : extraire le nombre disponible (ex: "In stock (22 available)" → 22)
    df["availability"] = df["availability"].str.extract(r"(\d+)").fillna(0).astype(int)

    # Convertir le rating texte en note chiffrée grâce au dictionnaire
    df["rating"] = df["rating"].map(rating_map).fillna(0).astype(int)

    return df
