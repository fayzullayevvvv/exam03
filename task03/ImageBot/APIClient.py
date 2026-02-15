import requests
import random


def dog_api():
    response = requests.get(
        "https://dog.ceo/api/breeds/image/random", params={"t": random.random()}
    )
    return response.json()["message"]


def cat_api():
    response = requests.get(
        "https://api.thecatapi.com/v1/images/search", params={"t": random.random()}
    )
    return response.json()[0]["url"]


def fox_api():
    response = requests.get(
        "https://randomfox.ca/floof/", params={"t": random.random()}
    )
    return response.json()["image"]
