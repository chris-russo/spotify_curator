# Spotify Curator

A Python 3.5.2 Flask API for curating Spotify playlists from a text search by Chris Russo.

## Setup

Before running this Flask API, install the project requirements by executing `$ pip install -r requirements.txt` in your shell. Run the API locally by executing `$ python app.py` in your shell from the root directory of this project.

## Endpoints

Once the API is running locally, you can submit POST requests to the Playlist Maker endpoint (/make_playlist) with the following command:

```
curl -X POST \
  http://127.0.0.1:5000/make_playlist \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -H 'postman-token: 327406e6-59df-8237-6a53-c61c33995a2c' \
  -F 'text=<KEYWORDS_GO_HERE>'
```

**Note:** Replace the value `<KEYWORDS_GO_HERE>` in the `text` key of the form body with whatever keywords you'd like.

  
The response is a JSON containing an array of tracks, i.e. Spotify URLs:

```
{
  "tracks": [
    "https://open.spotify.com/track/7JeKXMQKm6GoLGTkNy2jZ0",
    "https://open.spotify.com/track/5ZRxxnab9kLUqZPzoelgGP",
    "https://open.spotify.com/track/16uXqmSMAOl0MxtgVQTGeH"
  ]
}
```
