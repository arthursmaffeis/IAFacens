import shutil
import os

origem = "data/raw/data.csv"
destino = "data/bronze/job_data.csv"

os.makedirs("data/bronze", exist_ok=True)

shutil.copy(origem, destino)

print("Dados movidos para BRONZE")