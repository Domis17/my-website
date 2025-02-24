import requests
import json

def send_webhook_message(webhook_url, message):
    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")

def main():
    webhook_url = 'https://discord.com/api/webhooks/1343679739180613652/Hda-bTxbe3FiUiSvNLP4fSaUq7CK73qH3jQGJn1QqZJC_IGudIhkcAUau6G9YS55Zqo1'

    # Send initial message
    send_webhook_message(webhook_url, "Token grabber working, getting the token")

    # Simulate deployment process
    send_webhook_message(webhook_url, "Link is made")
    send_webhook_message(webhook_url, "Deploying...")
    send_webhook_message(webhook_url, "Deployment successful!")

    # Simulate token grabbing process
    send_webhook_message(webhook_url, "Token grabber working, getting the token")

if __name__ == "__main__":
    main()
