Introduction scraping de données
================================

Ce repo contient les notebooks correspondant au brief [La Plume Libre #3] Extraction de données automatisée pour le site d'une librairie en ligne.

# Projet de Scraping d'une Librairie

# Description

Ce projet Python scrape des données depuis un site de livres (titres, prix, stock, rating, etc.), les sauvegarde dans un fichier CSV, les nettoie et les insère dans une base de données SQLite.

L'organisation suit une structure professionnelle avec :
- `data/` : fichier.csv
- `get_data/` : scraping
- `process_data/` : nettoyage des données
- `database/` : insertion en base
- `pipelines/` : pipeline complet
- `main.py` : execute tout le pipeline

# Installer les dépendances

```bash
pip install -r requirements.txt
