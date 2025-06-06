import joblib
import numpy as np

modelo = joblib.load('ml_model/model.pkl')
mapa_inverso = {0: 'baixo', 1: 'medio', 2: 'alto'}

def prever_risco(dados):
    entrada = np.array([[dados['temperatura'], dados['umidade'], dados['precipitacao']]])
    risco = modelo.predict(entrada)[0]
    print("Nível de risco:", mapa_inverso[risco])

    if risco == 2:
        print("⚠️ Ação recomendada: evacuação imediata")
    elif risco == 1:
        print("⚠️ Ação recomendada: manter vigilância e preparar abrigos")
    else:
        print("✅ Situação estável, seguir monitorando")


