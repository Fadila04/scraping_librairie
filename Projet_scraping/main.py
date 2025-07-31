# main.py
import argparse

from pipeline_scrapping.pipeline_scraping import run_scraping_pipeline

if __name__ == "__main__":
    run_scraping_pipeline()

parser = argparse.ArgumentParser(description="Pipeline de scraping de livres")
parser.add_argument("--pages", type=int, default=1, help="Nombre de pages à scraper")
args = parser.parse_args() 


