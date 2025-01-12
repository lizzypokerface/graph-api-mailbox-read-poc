import webbrowser
import msal
import requests

# Configuration
CLIENT_ID =""
CLIENT_SECRET = ""
SCOPES = ["Mail.Read", "User.Read"]
MAILBOX = "lizzypokerface@outlook.com"
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0/"

# authentication with authorization code
authority_url = "https://login.microsoftonline.com/consumers/"
client_instance = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=authority_url,
)

authorization_requests_url = client_instance.get_authorization_request_url(SCOPES)
webbrowser.open(authorization_requests_url,new=True)
authorization_code =input("Enter Authorization Code: ")

access_token = client_instance.acquire_token_by_authorization_code(
    code=authorization_code,
    scopes=SCOPES
    )

access_token_id = access_token["access_token"]
headers = {"Authorization": "Bearer " + access_token_id}

# https://graph.microsoft.com/v1.0/users/lizzypokerface@outlook.com/messages
url = f"{GRAPH_API_ENDPOINT}/users/{MAILBOX}/messages"
response = requests.get(url, headers=headers)

print(response)
print(response.json())
