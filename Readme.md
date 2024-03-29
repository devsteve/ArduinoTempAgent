Basic script to listen to data stream over USB serial port, from Ardunio. 
Intended to be persistently ran on controller Raspberry Pi

-Setup-

Create a init script:

vim /home/user/startup.sh

#!/bin/sh
python path/to/seriallistener.py  

Add to Cron:

$ crontab -e
@reboot  /home/user/startup.sh


- Script Source -

This script was created entirely by Chat GPT from the following input:

Create a python server script that listens on usb serial port for pattern humidity:{0-9}\.{0-9},temp:{0-9}\.{0-9} json serialises the result and posts it to a https endpoint

Additional ChatGPT provided detail:

Here's how it works:
•	The serial module is used to open the USB serial port specified by the ser variable.
•	A regular expression pattern is created to match lines that contain "humidity:" followed by a decimal number, followed by ",temp:" and another decimal number.
•	The script enters an infinite loop and reads lines from the serial port.
•	If a line matches the pattern, the script extracts the humidity and temperature values and creates a Python dictionary with these values.
•	The dictionary is then serialized to JSON using the json module.
•	The JSON data is sent to the HTTPS endpoint specified by the requests.post function, and the response from the endpoint is printed to the console.
Note that you'll need to replace the "https://your.endpoint.url" string with the actual URL of the endpoint that you want to send the data to. Also, make sure that you have the requests module installed before running the script. You can install it using pip install requests.
