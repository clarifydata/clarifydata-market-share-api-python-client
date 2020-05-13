import json

import requests


def get_market_share(
    sparte_or_category,
    postcodes_with_cust_amounts,
    gfk_weight=0,
    gas_avail_default_factor=0.5,
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
    :param gas_avail_default_factor: factor of available gas connections relative to
    electricity connections
    :param host: path to the API
    :param version: specify which version to use
    :return: dictionary with PLZ as keys and calculated market share as values
    """
    base_url = f"http://{host}/{version}/market_share/{sparte_or_category}"
    params = {
        "gfk_weight": gfk_weight,
        "gas_avail_default_factor": gas_avail_default_factor,
    }
    return _get_response(postcodes_with_cust_amounts, base_url, params)


def _get_response(postcodes_with_cust_amounts, base_url, params=None):
    data = json.dumps(postcodes_with_cust_amounts)
    response = requests.post(
        base_url,
        params=params,
        data=data,
        headers={
            "content-type": "application/json",
            "user-agent": "clarifydata-market-share-api-python-client",
            "accept": "application/json",
        },
    )
    if _is_valid_response(response):
        return json.loads(response.content)
    else:
        return None


def _is_valid_response(response):
    cont_type = response.headers.get("Content-Type", None)
    if cont_type != "application/json":
        return False
    if response.status_code != 200:
        return False
    return True
