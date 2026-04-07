import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow

# carregar dados
df = pd.read_csv("data/silver/job_data_clean.csv")

# reduzir tamanho (pra não pesar)
df = df.head(2000)

# entrada e saída
X = df["Description"]
y = df["Job Title"]

# transformar texto em número
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)

# modelo
model = LogisticRegression(max_iter=1000)

# MLflow
mlflow.set_tracking_uri("http://localhost:3000")
mlflow.set_experiment("job-classification")

with mlflow.start_run():

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Acurácia: {acc}")

    # log no MLflow
    mlflow.log_metric("accuracy", acc)