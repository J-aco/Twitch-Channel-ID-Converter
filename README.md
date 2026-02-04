# Twitch Channel ID to Channel Name Lookup

A simple Python script that looks up a **Twitch Channel ID** and returns the **channel (broadcaster) name** using the official Twitch Helix API.

**Notes**:
- Handles OAuth authentication (Client Credentials flow)
- Uses the Twitch **Helix API** (Kraken is deprecated)
- No OAuth scopes are required
- Access token is generated at runtime

---

## Requirements

- Python **3.7+**
- A Twitch Developer application
- Python package:
  - `requests`

Install dependencies:

```bash
pip install requests
```

---

## Twitch API Setup

1. Go to the Twitch Developer Console:
   https://dev.twitch.tv/console/apps/create

2. Create a new application (Below details can be used for a one time use/random test app)
   - **Name**: Any unique name
   - **OAuth Redirect URL**: https://localhost
   - **Category**: Other

3. Copy the **Client ID**

4. Generate and copy the **Client Secret**

## Configuration

Edit the script and update the following values:

```python
CHANNEL_ID = '123456789'
client_id = 'Insert Client ID here'
client_secret = 'Insert Secret here'
```

- `CHANNEL_ID`: Numeric Twitch broadcaster ID
- `client_id`: Twitch application Client ID
- `client_secret`: Twitch application Client Secret

