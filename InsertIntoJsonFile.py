import json
import os

from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


client_details = []
client_details = client_details

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

client_details = {"client_id" : client_id,
                  "client_secret":  client_secret }

print(client_details)

with open("client_codes_Spotify.json", "w") as f:
    json.dump(client_details, f)

