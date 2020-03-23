import json

import requests


BASE_URL = "http://127.0.0.1:5000/api/v1/plz_to_market_share"


def get_market_share_category(category, plz_with_cust_amounts):
    url = f"{BASE_URL}/{category}"
    data = json.dumps(plz_with_cust_amounts)
    response = requests.post(
        url, data=data, headers={"content-type": "application/json"}
    )
    return json.loads(response.content)


def get_market_share_sparte(sparte, plz_with_cust_amounts):
    url = f"{BASE_URL}/{sparte}"
    data = json.dumps(plz_with_cust_amounts)
    response = requests.post(
        url, data=data, headers={"content-type": "application/json"}
    )
    return json.loads(response.content)
