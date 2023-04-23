import webbrowser
import datetime
import requests
import pyautogui
import time
import serial

ser = serial.Serial('COM5', 9600)

# Define the list of URLs to choose from
urls = {
    '1': ('https://radio.coolsite.co.il/m.php?radio=8', 'Galgalz'),
    '2': ('https://radio.coolsite.co.il/m.php?radio=6', 'Galey Tzahal'),
    '3': ('https://radio.coolsite.co.il/m.php?radio=1', 'Eco-88')
}

# Ask the user for the time and URL choice
time_input = input("Enter time in HH:MM format: ")
time_input_parts = time_input.split(':')
hours = int(time_input_parts[0])
minutes = int(time_input_parts[1])
now = datetime.datetime.now()
alarm_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)

print("Choose a Station:")
for key, value in urls.items():
    print(f"{key}. {value[1]}")
url_choice = input()

# Calculate the time delay to the alarm_time
time_diff = alarm_time - datetime.datetime.now()
time_delay = time_diff.total_seconds()
#parameter to send to activate arduino
activate = 1

print(time_delay)
# Wait for the time delay and open the URL
if(time_delay > 0):
    time.sleep(time_delay)

ser.write(str(activate).encode())
# Open the URL and click the "Play" button
webbrowser.open(urls[url_choice][0])
time.sleep(5)
pyautogui.moveTo(525, 330)
pyautogui.click()