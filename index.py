from mqtt_listener import get_sensor_data
from use_ml import prever_risco

def main():
    print("🔄 Recebendo dados do ESP32...")
    dados = get_sensor_data()

    print("📊 Dados recebidos:")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

    print("\n🧠 Analisando risco com Machine Learning...")
    prever_risco(dados)

if __name__ == '__main__':
    main()