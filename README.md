# ISS Overhead Notifier

This Python script continuously checks if the International Space Station (ISS) is passing over your location at night. If so, it sends an email notification to alert you to look up.

## Features
- Fetches real-time ISS position using the Open Notify API.
- Retrieves local sunrise and sunset times from the Sunrise-Sunset API.
- Compares ISS coordinates with your location.
- Runs in a loop, checking every 60 seconds.
- Sends an email alert if the ISS is overhead and it's nighttime.

## Requirements
- Python 3.x
- `requests` library
- `smtplib` for email notifications
- Gmail account with "App Passwords" enabled

## Setup Instructions

1. Install required dependencies:
   ```bash
   pip install requests
   ```

2. Update the following variables in the script with your details:
   ```python
   MY_LAT = 43.135114  # Your latitude
   MY_LONG = 17.858345  # Your longitude
   MY_EMAIL = "your_email@gmail.com"  # Your Gmail address
   MY_PASSWORD = "your_app_password"  # App password for Gmail
   REC_EMAIL = "recipient_email@gmail.com"  # Email to receive alerts
   ```

3. Run the script:
   ```bash
   python script.py
   ```

## How It Works
1. The script fetches the ISS’s current latitude and longitude.
2. It checks if the ISS is near your location.
3. It retrieves sunrise and sunset times for your location.
4. The script runs in an infinite loop, checking every 60 seconds.
5. If the ISS is overhead during nighttime, an email alert is sent.

## Notes
- To send emails via Gmail, you must generate an "App Password" from your Google account security settings.
- Running the script continuously increases the chances of catching the ISS overhead.
- To stop the script, use `Ctrl + C` in the terminal.

## License
This project is free to use and modify.
