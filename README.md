# Spotify Curator

A Python 3.5.2 Flask API for curating Spotify playlists from a text search by Chris Russo.

## Setup

Before running this Flask API, install the project requirements by executing `$ pip install -r requirements.txt` in your shell. Run the API locally by executing `$ python app.py` in your shell from the root directory of this project.

## Endpoints

### Playlist: `/playlist`

#### Request

Once the API is running locally, you can submit POST requests to the Playlist endpoint (`/playlist`) with the following command:

```
curl -X POST \
  http://127.0.0.1:5000/playlist \
  -H 'Authorization: Bearer <OAUTH_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
	"text": "<KEYWORDS>"
}'
```

**Notes:** 

- Replace `<OAUTH_TOKEN>` in the `Authorization` header with your Spotify OAuth token. You can retrieve this token [here](https://developer.spotify.com/console/get-search-item/): 
  - Scroll down and select the "Get Token" button.  
  - Select "Request Token". No scopes are required, so you do not have to check any of these options.
  - Sign into your Spotify account and agree to Spotify's Developers: Console privacy policy.
  - You will be redirected back to the Search endpoint page and the `OAuth Token` field will now be filled in with your unique token.
- Replace `<KEYWORDS>` in the `text` data field with whatever keywords you'd like. Try something like "You are the best thing tonight baby tomorrow I'll be gone"

#### Response

The response is a JSON containing an array of tracks, i.e. Spotify URLs:

```
{
    "tracks": [
        "https://open.spotify.com/track/3taYFqoXR24xoIExLuQFRt",
        "https://open.spotify.com/track/7dvg5YratVoM7s8LoZp26D",
        "https://open.spotify.com/track/5LDsZVmr1qrPELnqdo6rzw",
        "https://open.spotify.com/track/1ZAP6PRNrAUcnbFCfuW2mb"
    ]
}
```
