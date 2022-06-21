import paho.mqtt.client as mqttclient
import time
import json
from chatbot import BlenderBot
from datetime import datetime
import t5


BROKER_ADDRESS = "demo.thingsboard.io"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "8YuJeWyjIJCUZZMymToz"
chatbot = BlenderBot()
conversation = []


def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


data = {'ok': True, 'done': True, 'success': True, 'data': [{'stdout':''}]}


def recv_message(client, userdata, received_data):
    global data
    print("Received: ", received_data.payload.decode("utf-8"))
    jsonobj = json.loads(received_data.payload)
    try:
        request_id = received_data.topic[len('v1/devices/me/rpc/request/'): len(received_data.topic)]

        if jsonobj["method"] == 'sendCommand':
            message = jsonobj['params']['command']
            conversation.append(message)

            if 'translate' in message.lower():
                response = t5.reply("translate English to German: ", message.split(': ')[1])
            elif 'summarize' in message.lower():
                response = t5.reply("summarize: ", message.split(': ')[1])
            elif 'acceptable' in message.lower():
                response = t5.reply("cola sentence: ", message.split(': ')[1])
            else:
                response = chatbot.reply(message)

            conversation.append(response)

            data['data'][0]['stdout'] = response

        client.publish('v1/devices/me/rpc/response/' + request_id, json.dumps(data), 1)
    except:
        pass


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("v1/devices/me/rpc/request/+")
    else:
        print("Connection failed")


client = mqttclient.Client("Gateway_Thingsboard")
client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)
client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883)
client.loop_start()
client.on_subscribe = subscribed
client.on_message = recv_message


while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    collected_data = {'Current time': current_time, 'a': 'z', 'Conversation length': len(conversation)}

    client.publish('v1/devices/me/telemetry', json.dumps(collected_data), 1)
    time.sleep(4)