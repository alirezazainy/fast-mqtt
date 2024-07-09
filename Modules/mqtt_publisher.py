import random
import time

from paho.mqtt import client as mqtt_client
from paho.mqtt.enums import CallbackAPIVersion


# broker = 'mqtt.samacontrol.com'
# port = 31512
# topic = "SERVER/#"
# # generate client ID with pub prefix randomly
# client_id = f'python-mqtt-{random.randint(0, 1000)}'
# # # username = 'emqx'
# # # password = 'public'

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, response_code, property):
        if response_code == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", response_code)

    client = mqtt_client.Client(CallbackAPIVersion.VERSION2, client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client: mqtt_client.Client, message: str):
    time.sleep(1)
    published_message = f"messages: {message}"
    result = client.publish(topic, published_message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{published_message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
 

CLIENT = connect_mqtt()
async def run():
    CLIENT.loop_start()
    # publish(client, input_message)
    # client.loop_stop()

async def send(msg):
    publish(CLIENT, msg)