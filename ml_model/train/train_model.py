import os
import pandas as pd
from pymongo import MongoClient
from sklearn.ensemble import RandomForestClassifier
import joblib

# Configurações via variáveis de ambiente
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
MONGO_DB = os.getenv("MONGO_DB", "enchentes")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "leituras")

# Conexão MongoDB
client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
db = client[MONGO_DB]
colecao = db[MONGO_COLLECTION]

# Carregar dados salvos
cursor = colecao.find()
dados = list(cursor)
df = pd.DataFrame(dados)

# Verifica se há dados suficientes
if df.empty or not all(col in df.columns for col in ['temperatura', 'umidade', 'precipitacao', 'risco_classe']):
    raise ValueError("Dados insuficientes ou campos ausentes no MongoDB.")

# Treinar novamente (adaptar conforme campos)
X = df[['temperatura', 'umidade', 'precipitacao']]
y = df['risco_classe']

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X, y)

# Ajuste do caminho para salvar o modelo na pasta correta
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model.pkl')
joblib.dump(modelo, model_path)
print('Novo modelo salvo em:', model_path)