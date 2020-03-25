from setuptools import setup

setup(
    name="plzwrapper",
    version="0.1",
    url="https://github.com/clarifydata/plz_service_api_wrapper",
    packages=["plzwrapper"],
    install_requires=[
        "certifi==2019.11.28",
        "chardet==3.0.4",
        "idna==2.9",
        "requests==2.23.0",
        "urllib3==1.25.8",
    ],
)
