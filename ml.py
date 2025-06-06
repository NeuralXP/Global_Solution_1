import pandas as pd
import numpy  as np
from sklearn.ensemble        import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics         import classification_report
import joblib
import os

# Dados sintéticos
np.random.seed(42)
n  =300

df =pd.DataFrame({
    'temperatura':  np.random.uniform(15, 40, n ),
    'umidade':      np.random.uniform(20, 100, n),
    'precipitacao': np.random.uniform(0, 300, n )
})

# Regras para risco
def definir_risco(row):
    if row['precipitacao']   >200:
        return 'alto'
    elif row['precipitacao'] >100 and row['umidade'] >80:
        return 'medio'
    else:
        return 'baixo'

df['risco'] =df.apply(definir_risco, axis=1)

# Transformar risco em números
mapa_risco         ={'baixo': 0, 'medio': 1, 'alto': 2}
df['risco_classe'] =df['risco'].map(mapa_risco)

# Treino
X                                =df[['temperatura', 'umidade', 'precipitacao']]
y                                =df['risco_classe']
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.2, random_state=42)

modelo                           =RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Avaliação
y_pred =modelo.predict(X_test)
print(classification_report(y_test, y_pred, target_names=mapa_risco.keys()))

# Exporta modelo
os.makedirs('ml_model', exist_ok=True)
joblib.dump(modelo, 'ml_model/model.pkl')
print      ('Modelo salvo em ml_model/model.pkl')