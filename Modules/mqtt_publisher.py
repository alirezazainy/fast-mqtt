import random
import time

from paho.mqtt import client as mqtt_client
from paho.mqtt.enums import CallbackAPIVersion

# Define results dictionary
RESULT = {
    "response_code": None,
    "response_message": None,
    "broker_server": None,
    "port": None,
    "topic": None,
    "client_id": None,
    
}

# broker = 'mqtt.samacontrol.com'
# port = 31512
# topic = "SERVER/#"
# # generate client ID with pub prefix randomly
# client_id = f'python-mqtt-{random.randint(0, 1000)}'
# # # username = 'emqx'
# # # password = 'public'

RESULT.update({"broker_server": 'broker.emqx.io'})
RESULT.update({"port": 1883})
RESULT.update({"topic": "python/mine"})
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
RESULT.update({"client_id": client_id})
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client.Client:
    """
    This function sets server credentials for client to connecting together

    Returns:
        mqtt_client.Client: type of mqtt client for messaging
    """
    def on_connect(client, user_data, flags, response_code, properties):
        """
        This function sets connection credentials for client on first connecting time and control connection

        Args:
            client (mqtt_client.Client): type of mqtt client for messaging
            user_data : client credentials
            flags : flags for messaging
            response_code : response code of first connection
            property : properties of client connection
        """
        RESULT.update({"response_code": response_code})
        if response_code == 0:
            RESULT.update({"response_message": "Connected to MQTT Broker!"})
        else:
            RESULT.update({"response_message": f"Failed to connect, return code {response_code}"})

    client = mqtt_client.Client(CallbackAPIVersion.VERSION2, client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(RESULT.get("broker_server"), RESULT.get("port"))
    return client


def publish(client: mqtt_client.Client, message: str) -> str:
    """
    This function publish a message and send it to broker

    Args:
        client (mqtt_client.Client): type of mqtt client for messaging
        message (str): mqtt operation

    Returns:
        str: returns a published message string
    """
    published_message = f"messages: {message}"
    result = client.publish(RESULT.get("topic"), published_message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        return f"Send `{published_message}` to topic `{RESULT.get("topic")}`"
    else:
        return f"Failed to send message to topic {RESULT.get("topic")}"
 
 # Define a client
CLIENT = connect_mqtt()
async def run() -> dict:
    """
    This function runs a mqtt connection and set a connection living loop

    Returns:
        dict: returns the connection result dictionary
    """
    CLIENT.loop_start()
    return RESULT

async def send(message: str) -> str:
    """
    This function send a message to publish and send to broker

    Args:
        message (str): mqtt operation

    Returns:
        str: returns a published message string
    """
    return publish(CLIENT, message)