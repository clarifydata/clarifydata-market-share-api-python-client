import json

import requests


BASE_URL = "http://127.0.0.1:5000/v1/plz_to_market_share"


def get_market_shares(type, plz_with_cust_amounts):
    url = f"{BASE_URL}/{type}"
    data = json.dumps(plz_with_cust_amounts)
    response = requests.post(
        url, data=data, headers={"content-type": "application/json"}
    )
    return json.loads(response.content)
