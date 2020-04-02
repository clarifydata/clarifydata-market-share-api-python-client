import json

import requests


BASE_PATH = "http://127.0.0.1:5000/api"
MARKET_SHARE_ENDPOINT = "v1/market_share"


def get_market_shares(type, plz_with_cust_amounts, gfk_weight=0):
    """
    Get market share for different categories (Strom, Gas, ...)
    and "Sparten" (Energie, Tel)
    :param type: Strom, Gas, Energie, FN (Festnetz), MF (Mobilfunk), Tel
    :param plz_with_cust_amounts: Dictionary containing PLZ
    as keys and corresponding customer amounts as values
    :param gfk_weight: weight of gfk data in calculated results
    :return: dictionary with PLZ as keys and calculated market share as values
    """
    url = f"{BASE_PATH}/{MARKET_SHARE_ENDPOINT}/{type}"
    if gfk_weight != 0:
        url += f"?gfk_weight={gfk_weight}"
    data = json.dumps(plz_with_cust_amounts)
    response = requests.post(
        url, data=data, headers={"content-type": "application/json"}
    )
    return json.loads(response.content)
