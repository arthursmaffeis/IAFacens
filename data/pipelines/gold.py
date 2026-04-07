import pandas as pd
import os

# lê dados do silver
df = pd.read_csv("data/silver/job_data_clean.csv")

# cria uma coluna única com tudo junto
df["text"] = df["Job Title"] + " - " + df["Description"]

# cria pasta gold
os.makedirs("data/gold", exist_ok=True)

# salva só o que importa
df_gold = df[["text"]]

df_gold.to_csv("data/gold/job_data_gold.csv", index=False)

print("Dados preparados para GOLD")