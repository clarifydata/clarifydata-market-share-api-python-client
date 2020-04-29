# Clarifydata Market Share Python API Client

Wrap calls to Clarifydata Market Share REST endpoints.

## Installation
- Clone project
    ```shell
    $ git clone https://github.com/clarifydata/clarifydata-market-share-api-python-client
    ```
- install with `pip`
    ```shell
    $ cd clarifydata-market-share-api-python-client
    $ pip install .
    ```

## Usage
```python3
>>> import cdmarketshare
>>> market_share = cdmarketshare.get_market_share(
        "Strom",
        {<some_postcode>: <some_customer_amount>}
    )
```


## Development
- Install dependencies with [pipenv](https://pipenv.pypa.io/en/latest/):
    ```shell
    $ pipenv install --dev
    ```
- sync dependencies between Pipfiles and setup.py
    ```shell
    $ pipenv run pipenv-setup sync
    ```
