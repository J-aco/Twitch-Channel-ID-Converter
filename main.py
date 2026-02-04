import requests
import json

#Enter Channel ID to look up here
CHANNEL_ID = '123456789'

#Enter Twitch Application details here - refer to readme for guide.
client_id = 'Insert Client ID here'
client_secret = 'Insert Secret here'

#Auth to get access token
url = 'https://id.twitch.tv/oauth2/token'
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
}
response = requests.post(url, data=payload)
access_token = json.loads(response.text)['access_token']

#Build and make API request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Client-Id': client_id,
}
url = f'https://api.twitch.tv/helix/channels?broadcaster_id={CHANNEL_ID}'
response = requests.get(url, headers=headers)
data = json.loads(response.text)

#Return the name
print(data['data'][0]['broadcaster_name'])
