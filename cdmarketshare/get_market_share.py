import json

import requests


def get_market_share(
    sparte_or_category,
    postcodes_with_cust_amounts,
    gfk_weight=0,
    host="market-share.clarifydata.de",
    version="v1",
):
    """
    Get market share for different categories (Strom, Gas, ...)
    and "Sparten" (Energie, Tel)
    :param sparte_or_category: Strom, Gas, Energie, FN (Festnetz), MF (Mobilfunk), Tel
    :param postcodes_with_cust_amounts: Dictionary containing postcodes
    as keys and corresponding customer amounts as values
    :param gfk_weight: weight of gfk data in calculated results
    :param host: path to the API
    :param version: specify which version to use
    :return: dictionary with PLZ as keys and calculated market share as values
    """
    url = f"http://{host}/{version}/market_share/{sparte_or_category}"
    if gfk_weight != 0:
        url += f"?gfk_weight={gfk_weight}"
    data = json.dumps(postcodes_with_cust_amounts)
    response = requests.post(
        url,
        data=data,
        headers={
            "content-type": "application/json",
            "user-agent": "clarifydata-market-share-api-python-client",
            "accept": "application/json",
        },
    )
    return json.loads(response.content)
