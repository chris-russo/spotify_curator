"""
Spotify Curator

Spotify Curator is a Flask API that generates a playlist of track titles 
(Spotify URLs) from text submitted by a user.

For example, the text "If I can't let it go out of my mind" may return the
playlist:

  1. http://open.spotify.com/track/6mcu7D7QuABVwUGDwovOEh
  2. http://open.spotify.com/track/5ZRxxnab9kLUqZPzoelgGP
  3. http://open.spotify.com/track/3L0bYyI0FHRiD1xZfbZedz


Spotify API Endpoint Reference: Search
https://developer.spotify.com/web-api/search-item/

# Example URL to find track At Your Funeral by Saves the Day:
# "https://api.spotify.com/v1/search?q="at+your+funeral"+artist:saves+the+day&type=track"


API order of operations:
  - Clean text input, i.e. keep alphanumeric characters only
  - Create URL string from text
  - Use Spotify API Endpoint Search to search for track titles like text input
  - Parse through search results and key-value pairs of track titles and
    external Spotify URL
  - Ensure output playlist track titles matches order of text input

"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

# Instantiate Flask app and API objects
app = Flask(__name__)
api = Api(app)

# Create request parser object
parser = reqparse.RequestParser(bundle_errors=True)

# Add data POST argument to parser
parser.add_argument('text', type=str, location='form')


# Regex substitute any non-alphanumeric characters with a space
# re.sub('[^a-zA-Z0-9_]', ' ', x.lower()).split(' ')


# Create playlist maker class
class PlaylistMaker(Resource):
    """
    Playlist maker class
    
    Allows a user to POST a text which is used to make a playlist of Spotify 
    tracks using the Spotify API
    """

    def post(self):
        args = parser.parse_args(strict=True)
        response = args

        return response.text + ' from space.'


# Set up API source routing
api.add_resource(PlaylistMaker, '/make_playlist')


if __name__ == "__main__":
    app.run(debug=True)
