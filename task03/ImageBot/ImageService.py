from .APIClient import dog_api, cat_api, fox_api


def fetch_random_image(animal: str) -> str:
    img_url = None

    if animal == "dog":
        img_url = dog_api()
    elif animal == "cat":
        img_url = cat_api()
    elif animal == "fox":
        img_url = fox_api()

    return img_url
