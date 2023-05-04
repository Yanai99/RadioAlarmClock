import webbrowser
import datetime
import requests
import pyautogui
import time
import serial

def seconds_to_hours_minutes(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return int(hours), int(minutes)


ser = serial.Serial('COM5', 9600)

activate = 1
wake_up = 2

# Define the list of URLs to choose from
urls = {
    '1': ('https://tunein.com/radio/Joint-Radio-Blues-s203399/', 'Joint Radio Blues'),
    '2': ('https://tunein.com/radio/KAN-88-880-s100340/', 'Kan 88'),
    '3': ('https://tunein.com/radio/Juice-Belfast-1038-s297336/', 'Juice Belfast')
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
ser.write(str(activate).encode())

# Calculate the time delay to the alarm_time
time_diff = alarm_time - datetime.datetime.now()
time_delay = time_diff.total_seconds()
#parameter to send to activate arduino

hours, minutes = seconds_to_hours_minutes(time_delay)
print(f"we'll wake you up in {hours} hours and {minutes} minutes")

# Wait for the time delay and open the URL
if(time_delay > 0):
    time.sleep(time_delay)

ser.write(str(wake_up).encode())
# Open the URL and click the "Play" button
webbrowser.open(urls[url_choice][0])