# Twitch Channel ID to Channel Name Lookup

A simple Python script that uses a **Twitch Channel ID** and returns the **Channel name** (Broadcaster Name)

**Notes**:
- Requires [Twitch Dev App](#twitch-app-setup) for API
- Handles OAuth (Client Credentials flow)
- Uses the Twitch **Helix API** (Kraken is deprecated)
- No OAuth scopes are required
- Access token is generated at runtime and isnt stored.


## Requirements

- Python **3.7+**
- [A Twitch Developer application](#twitch-app-setup)
- Python package:
  - `requests`

Install dependencies:

```bash
pip install requests
```

## Twitch App Setup

1. Go to the Twitch Developer Console:
   https://dev.twitch.tv/console/apps/create

2. Create a new application (Below details can be used for a one time use/random test app)
   - **Name**: Any unique name
   - **OAuth Redirect URL**: https://localhost
   - **Category**: Other

3. Copy the **Client ID** into the script

4. Click "New Secret" and copy the **Client Secret** into the script

## Configuration

Edit the script and update the following values:

```python
CHANNEL_ID = '123456789'
client_id = 'Insert Client ID here'
client_secret = 'Insert Secret here'
```

- `CHANNEL_ID`: Numeric Twitch broadcaster ID as a string
- `client_id`: Alpha-numeric Client ID as a string
- `client_secret`: Alpha-numeric Client Secret as a string

# License

MIT License
