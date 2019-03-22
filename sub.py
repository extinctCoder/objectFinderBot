import paho.mqtt.client as mqtt
import time
broker_address="192.168.0.102"

topic =  "#"

def on_message(client, userdata, message):
    print("Message received: ", str(message.payload))
    print("Message topic: ", message.topic)
    print("Message qos: ", message.qos)
    print("Message retain flag: ", message.retain)
    pass
def on_log(client, userdata, level, buf):
    print("Log: ", buf)
    pass
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print ("Mqtt client connected with broker")
        client.subscribe(topic)
    else:
        print ("Unable to connect with broker. Error code:", rc)

print("Wellcome to mqtt broker subscribe script")
print("Creating new instance of mqtt client")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log
print("Connecting to mqtt broker")
client.connect(broker_address)
client.loop_forever()
