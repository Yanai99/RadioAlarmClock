import webbrowser
import datetime
import requests
import pyautogui
import time

# Define the list of URLs to choose from
urls = {
    '1': 'https://radio.coolsite.co.il/m.php?radio=8',
    '2': 'https://radio.coolsite.co.il/m.php?radio=6',
    '3': 'https://radio.coolsite.co.il/m.php?radio=1'
}

# Ask the user for the time and URL choice
time_input = input("Enter time in HH:MM format: ")
time_input_parts = time_input.split(':')
hours = int(time_input_parts[0])
minutes = int(time_input_parts[1])
now = datetime.datetime.now()
alarm_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)

print("Choose a URL:")
for key, value in urls.items():
    print(f"{key}. {value}")
url_choice = input()

# Open the URL and click the "Play" button
response = requests.get(urls[url_choice])
webbrowser.open(urls[url_choice])
time.sleep(5)
pyautogui.moveTo(525, 330)
pyautogui.click()