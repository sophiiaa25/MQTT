import paho.mqtt.client as mqtt
# Unidade Curricular - Redes IoT

broker = "broker.hivemq.com"  # Broker público
port = 1883
topic = "senai/dev"

client = mqtt.Client()
client.connect(broker, port)

while True:
    mensagem = input("Digite uma mensagem para enviar: ")
    client.publish(topic, mensagem)
    print(f"Mensagem '{mensagem}' publicada no tópico '{topic}'")