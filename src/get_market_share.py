import json

import requests


def get_market_share_from_api(type, plz_with_cust_amounts):
    url = f"http://127.0.0.1:5000/api/v1/plz_to_market_share/{type}"
    data = json.dumps(plz_with_cust_amounts)
    response = requests.post(
        url, data=data, headers={"content-type": "application/json"}
    )
    return json.loads(response.content)
