import pandas as pd
import os

# lê dados da bronze
df = pd.read_csv("data/bronze/job_data.csv")

# remove linhas vazias
df = df.dropna()

# deixa tudo minúsculo (boa prática pra NLP)
df["Description"] = df["Description"].str.lower()

# cria pasta silver
os.makedirs("data/silver", exist_ok=True)

# salva
df.to_csv("data/silver/job_data_clean.csv", index=False)

print("Dados processados para SILVER 🚀")