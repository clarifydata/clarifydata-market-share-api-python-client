from setuptools import setup

setup(
    name="clarifydata-market-share-python-api-client",
    version="0.1",
    url="https://github.com/clarifydata/clarifydata-market-share-api-python-client",
    author="clarifydata GmbH",
    packages=["clarifydataapiclient"],
    install_requires=[
        "certifi==2019.11.28",
        "chardet==3.0.4",
        "idna==2.9",
        "requests==2.23.0",
        "urllib3==1.25.8",
    ],
)
