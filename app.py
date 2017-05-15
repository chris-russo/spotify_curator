"""
Spotify Curator

Spotify Curator is a Python 3.5.2 Flask API with a single endpoint. A POST 
request containing text made to the Playlist Maker endpoint ('/make_playlist') 
will return a playlist, i.e. a list of Spotify URLs. 

For example, the text "If I can't let it go out of my mind" may return the
playlist:

    {
      "tracks": [
        "https://open.spotify.com/track/7JeKXMQKm6GoLGTkNy2jZ0",
        "https://open.spotify.com/track/5ZRxxnab9kLUqZPzoelgGP",
        "https://open.spotify.com/track/16uXqmSMAOl0MxtgVQTGeH"
      ]
    }

See README for further details.

Spotify API Endpoint Reference: Search
https://developer.spotify.com/web-api/search-item/

# Example URL to find track At Your Funeral by Saves the Day:
# "https://api.spotify.com/v1/search?q="at+your+funeral"+artist:saves+the+day&type=track"


"""

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import requests
import json
import random
import re

# Instantiate Flask app and API objects
app = Flask(__name__)
api = Api(app)

# Create request parser object
parser = reqparse.RequestParser(bundle_errors=True)

# Add data POST argument to parser
parser.add_argument('text', type=str, location='form')


def create_url(query_string: str) -> str:
    url = 'https://api.spotify.com/v1/search?q="%s"&type=track' % query_string
    return url


def search_tracks(url: str) -> dict:
    response = requests.get(url)
    return json.loads(response.text)


# Create playlist maker class
class PlaylistMaker(Resource):
    """
    Playlist maker class
    
    Allows a user to POST a text which is used to make a playlist of Spotify 
    tracks using the Spotify API
    """

    def post(self):
        # Get text from POST body
        args = parser.parse_args(strict=True)
        text = args.text

        # Remove commas and apostrophes from text and split keywords into list
        keywords = re.sub(r'[\',]', "", text.lower()).split(' ')

        # Remove empty strings from list of keywords
        keywords = list(filter(None, keywords))

        # Create an empty list of remaining keywords to append to later on
        remaining_keywords = []

        # Create an empty list to append Spotify track URLs later on. This list
        # will be returned when a POST request is made to the 'make_playlist'
        # endpoint
        playlist = {'tracks': []}

        # Algorithm for creating playlist from keywords
        while len(keywords) > 0:
            # Create string of keywords to compare with track titles later on
            keywords_string = ' '.join(keywords)

            # Create query string to inject into Spotify API GET request
            query_string = '+'.join(keywords)

            # Make GET request to Spotify API Search endpoint
            url = create_url(query_string)
            data = search_tracks(url)

            # Create empty dictionary of tracks
            tracks = {}

            # Retrieve track name and track's Spotify URL from Spotify API
            # response data items list
            items = data['tracks']['items']

            for i in range(len(items)):
                track_i = items[i]['name']
                spotify_url_i = items[i]['external_urls']['spotify']
                tracks[track_i] = spotify_url_i

            # If no tracks matching keywords are found, update keywords and
            # remaining keywords lists and try again
            if tracks == {}:
                remaining_keywords.insert(0, keywords[-1])
                keywords = keywords[0:-1]

            # If tracks found, evaluate titles for matches with keywords
            else:
                # Create empty list of valid tracks from tracks dictionary
                keep_tracks = []

                # Append tracks with valid titles to list of tracks to keep
                # NOTE: A valid title is one that is identical to the keywords
                for title in list(tracks.keys()):
                    if re.sub(r'[\',]', "", title.lower()) == keywords_string:
                        keep_tracks.append(title)

                # Define logic for assessing list of valid track titles
                if len(keep_tracks) == 0:
                    # If no identical track titles found, update keywords and
                    # remaining keywords lists and try again
                    remaining_keywords.insert(0, keywords[-1])
                    keywords = keywords[0:-1]

                else:
                    # If identical track titles found, randomly select a track
                    # from list of valid tracks
                    keep_track = random.choice(keep_tracks)

                    # Append track Spotify URL to playlist
                    playlist['tracks'].append(tracks[keep_track])

                    # Update keywords and remaining keywords lists
                    keywords = remaining_keywords
                    remaining_keywords = []

        return jsonify(playlist)


# Set up API source routing
api.add_resource(PlaylistMaker, '/make_playlist')


if __name__ == "__main__":
    app.run(debug=True)
