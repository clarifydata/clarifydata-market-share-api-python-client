import json
import time
from typing import Dict, List

import requests

MAX_RETRIES = 10

DEFAULT_API_URL = "https://postcode.services.clarifydata.de"


def get_market_share(
    sparte_or_category,
    postcodes_with_cust_amounts,
    gfk_weight=0,
    gas_avail_default_factor=0.5,
    api_url=DEFAULT_API_URL,
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
    query_url = f"{api_url}/{version}/market_share/{sparte_or_category}"
    params = {
        "gfk_weight": gfk_weight,
        "gas_avail_default_factor": gas_avail_default_factor,
    }
    return _get_response_with_retry(postcodes_with_cust_amounts, query_url, params)


def get_household_count(
    postcodes_data: Dict[str, List[str]],
    gfk_weight=0,
    api_url=DEFAULT_API_URL,
    version="v1",
):
    """
    Get household count for given postcodes
    :param postcodes_data: {"plz": [<list of postcodes>]}
    :param gfk_weight: weight of GfK data, must be in [0, 1]
    :param host: path to the API
    :param version: specify which version to use
    :return: dictionary with PLZ as keys and household count as values
    """
    query_url = f"{api_url}/{version}/household_count"
    params = {"gfk_weight": gfk_weight}
    return _get_response_with_retry(postcodes_data, query_url, params)


def _get_response_with_retry(postcodes_with_cust_amounts, base_url, params):
    market_share = None
    for i in range(MAX_RETRIES):
        market_share = _get_response(postcodes_with_cust_amounts, base_url, params)
        if market_share is not None:
            break
        elif i < (MAX_RETRIES - 1):
            time.sleep(60)
    return market_share


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
