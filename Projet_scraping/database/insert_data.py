# insert_data.py
import sqlite3

# Fonction pour insérer les données dans la base de données
def insert_books_to_db(df, db_path="book_store.db"):
    # Connexion à la base de données 
    conn = sqlite3.connect(db_path)

    # Création du curseur pour exécuter des commandes SQL
    cursor = conn.cursor()

    # Création de la table 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_list (
            title TEXT,
            price REAL,
            availability INTEGER,
            rating INTEGER
        )
    """)

    # Insérer le DataFrame dans la table 'book_list'
    df.to_sql("book_list", conn, if_exists="replace", index=False)

    # Vérification : compter le nombre de lignes insérées
    cursor.execute("SELECT COUNT(*) FROM book_list")
    book_count = cursor.fetchone()[0]
    print(f"Nombre de livres dans la base de données : {book_count}")

