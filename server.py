import paho.mqtt.client as mqtt
import GPIO

def on_connect(client, user_data, flags, rc):
    print("Result Code: ", rc)
    client.subscribe("My_Home")

def on_message(client, user_data, msg):
    status = str(msg.payload)
    print("status:", status)
    if status == '1':
        GPIO.on()
    elif status == '0':
        GPIO.off()
    elif status == 'temp':
        temperature = GPIO.temp()
        client.publish('My_Home_Temp', temperature)
    elif status == 'hum':
        humidity = GPIO.hum()
        client.publish('My_Home_Hum', humidity)

client = mqtt.Client()

client.connect("iot.eclipse.org", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
