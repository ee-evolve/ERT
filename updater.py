import atoma
import requests

response = requests.get('http://lucumr.pocoo.org/feed.atom')
feed = atoma.parse_atom_bytes(response.content)
print(feed)
