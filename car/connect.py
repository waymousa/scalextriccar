# look at the phew library for micropython to create a rest api
# https://www.hackster.io/rajivcodelab/how-to-build-a-rest-api-on-raspberry-pi-pico-w-control-led-91b25b
# https://pypi.org/project/micropython-phew/

import time
import network
import rp2
rp2.country("GB")

ssid = ""
psk = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,psk)

max_wait = 30

while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("Waiting for a wifi connection...")
    time.sleep(1)
    
if wlan.status() != 3:
    raise RuntimeError("Network connection failed")
else:
    print("Connected to wifi network")
    print(wlan.ifconfig())