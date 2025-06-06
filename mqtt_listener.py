import json
import paho.mqtt.client as mqtt

sensor_data = {}
mensagem_recebida = False

def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com código:", rc)
    client.subscribe("fiap/gs/enchentes")

def on_message(client, userdata, msg):
    global sensor_data, mensagem_recebida

    try:
        payload = json.loads(msg.payload.decode())

        sensor_data = {
            'temperatura': payload["temperatura"],
            'umidade': payload["umidade"],
            'precipitacao': payload["precipitacao"]
        }

        mensagem_recebida = True
        client.disconnect()

    except Exception as e:
        print("Erro ao processar mensagem:", e)

#def get_sensor_data():
#    global sensor_data, mensagem_recebida

#    mensagem_recebida = False
#    sensor_data = {}

#    client = mqtt.Client()
#    client.on_connect = on_connect
#    client.on_message = on_message

#    print("🔌 Conectando ao broker MQTT...")
#    client.connect("broker.hivemq.com", 1883, 60)

#    client.loop_start()

#    while not mensagem_recebida:
#        pass

#    client.loop_stop()
#    return sensor_data


def get_sensor_data():
    return {
        'temperatura': 30.5,
        'umidade': 85.0,
        'precipitacao': 190.0
    }


