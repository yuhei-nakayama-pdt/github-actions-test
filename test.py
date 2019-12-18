import paho.mqtt.client as mqtt

def main():
  client = mqtt.Client() # type: mqtt.Client
  client.connect(host="mqtt", port=1883)
  print("Test ok")

if __name__ == "__main__":
  main()
