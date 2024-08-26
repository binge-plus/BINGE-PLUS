import os
import requests
import time

# Configuration
TELEGRAM_BOT_TOKEN = '6384770295:AAH_FlqDRXL49GM8eR5yH_WJ-K24Dsm5B4g'
TELEGRAM_CHAT_ID = '-1001715673902'  # Use '@channelname' or your channel ID
# TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TIMESTAMP_FILE = 'last_message_timestamp.txt'
COOL_DOWN_PERIOD = 12 * 60 * 60  # 12 hours in seconds

def can_send_message():
    """Check if the cooldown period has passed since the last message."""
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, 'r') as file:
            last_timestamp = float(file.read().strip())
        return time.time() - last_timestamp > COOL_DOWN_PERIOD
    return True

def update_timestamp():
    """Update the timestamp of the last message sent."""
    with open(TIMESTAMP_FILE, 'w') as file:
        file.write(str(time.time()))

def send_telegram_message(message):
    """Send a message to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print('Message sent successfully')
        update_timestamp()  # Update timestamp after successful send
    except requests.exceptions.RequestException as e:
        print(f'Failed to send message: {e}')

if __name__ == "__main__":
    if can_send_message():
        send_telegram_message("Binge+ Site Updated")
    else:
        print("Message not sent. Cooldown period has not yet passed.")
