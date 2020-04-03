import json

import requests


def get_market_shares(
    sparte_or_category,
    plz_with_cust_amounts,
    gfk_weight=0,
    base_path="http://market-share.clarifydata.de",
    version="1.0",
):
    """
    Get market share for different categories (Strom, Gas, ...)
    and "Sparten" (Energie, Tel)
    :param type: Strom, Gas, Energie, FN (Festnetz), MF (Mobilfunk), Tel
    :param plz_with_cust_amounts: Dictionary containing PLZ
    as keys and corresponding customer amounts as values
    :param gfk_weight: weight of gfk data in calculated results
    :param base_path: path to the API
    :param version: specify which version to use
    :return: dictionary with PLZ as keys and calculated market share as values
    """
    url = f"{base_path}/{version}/'market_share'/{type}"
    if gfk_weight != 0:
        url += f"?gfk_weight={gfk_weight}"
    data = json.dumps(plz_with_cust_amounts)
    response = requests.post(
        url, data=data, headers={"content-type": "application/json"}
    )
    return json.loads(response.content)
