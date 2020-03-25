import json

import requests


BASE_PATH = "http://127.0.0.1:5000/api"
MARKET_SHARE_ENDPOINT = "v1/plz_to_market_share"


def get_market_shares(type, plz_with_cust_amounts):
    """
    Get market share for different categories (Strom, Gas, ...)
    and "Sparten" (Energie, Tel)
    :param type: Strom, Gas, Energie, FN (Festnetz), MF (Mobilfunk), Tel
    :param plz_with_cust_amounts: Dictionary containing PLZ
    as keys and corresponding customer amounts as values
    :return: dictionary with PLZ as keys and calculated market share as values
    """
    url = f"{BASE_PATH}/{MARKET_SHARE_ENDPOINT}/{type}"
    data = json.dumps(plz_with_cust_amounts)
    response = requests.post(
        url, data=data, headers={"content-type": "application/json"}
    )
    return json.loads(response.content)
