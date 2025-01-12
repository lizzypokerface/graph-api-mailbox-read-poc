import msal
import json
import requests

# Configuration
CLIENT_ID = ""
CLIENT_SECRET = ""
TENANT_ID = ""

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default",
    }
    response = requests.post(url, data=payload)
    response_data = response.json()
    return response_data["access_token"]


def read_email():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    url = "https://graph.microsoft.com/v1.0/users/lizzypokerface@outlook.com/messages"
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        graph_data = response.json()
        print("SUCCESS")
        print(json.dumps(graph_data, indent=2))
    else:
        print("ERROR")
        print(response.text)


def send_email():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    url = "https://graph.microsoft.com/v1.0/users/lizzypokerface@outlook.com/sendMail"
    payload = {
        "message": {
            "subject": "Test mail sent using python",
            "body": {
                "contentType": "text",
                "content": "test mail generated using python",
            },
            "toRecipients": [{"emailAddress": {"address": "hithere@gmail.com"}}],
        },
        "saveToSentItems": "true",
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.text)


if __name__ == "__main__":
    access_token = get_access_token()
    # read_email()
    # send_email()
