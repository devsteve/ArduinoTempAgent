import serial
import re
import json
import requests

# Set up the serial connection (replace '/dev/ttyUSB0' with the correct serial port)
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Set up the regular expression pattern to match the expected data format
pattern = re.compile(r'humidity:(\d+\.\d+),temp:(\d+\.\d+)')

# Set up the HTTPS endpoint URL to post the data to
url = 'https://localhost:49153/temp'

# Continuously read data from the serial port
while True:
    # Read a line of data from the serial port
    data = ser.readline().decode().strip()

    # If the data matches the expected pattern, extract the values and serialize as JSON
    match = pattern.match(data)
    if match:
        humidity = float(match.group(1))
        temp = float(match.group(2))
        payload = json.dumps({'humidity': humidity, 'temp': temp})

        # Send the JSON payload to the HTTPS endpoint
        print(payload);
        response = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})
        print(response.status_code)