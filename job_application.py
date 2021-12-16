# REFERENCE: GET and POST requests using Python
# https://www.geeksforgeeks.org/get-post-requests-using-python/

# REFERENCE: Post JSON using Python Requests
# https://bit.ly/2w6YHGa

import requests
import json

url = "https://contact.plaid.com/jobs"

data = {
    'name': 'Youngil Kim',
    'email': 'youngilkim822@gmail.com',
    'resume': 'https://drive.google.com/file/d/1FlzUNXLCiKPuXLHyzWifHxPcIZ4Eo5Iq/view?usp=sharing',
    "phone": "917-517-0393",
    "job_id": "0aa2328f-611b-4bfe-8920-0188819dfb96",
    'github': 'https://github.com/rladuddlf',
    'linkedin': 'https://www.linkedin.com/in/young-il-kim-237944213/',
    'youtube': 'https://www.youtube.com/channel/UCYLItBQe5mREFJNmZe5qVBw',
    'location': "New York, NY
    'favorite candy': 'Butterfinger',
    'superpower': 'Wingsuit Pilot'
}
data = json.dumps(data)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

http_post_request = requests.post(url=url, data=data, headers=headers)

server_response = http_post_request.text

print(server_response)
