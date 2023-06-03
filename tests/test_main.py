from fastapi.testclient import TestClient
import pytest

from src.utils.feelings import feelings

from PIL import Image
import numpy as np
import random
import os

from main import app


@pytest.fixture
def client():
    return TestClient(app)

def save_image(filename: str):
    rgb_array = np.random.rand(255, 255, 3) * 255
    image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')
    image.save(os.path.join(os.getcwd(), filename))


def test_is_feeling_match(client):
    filename = "test.jpg"
    save_image(filename)

    image_path = f"{os.getcwd()}/{filename}"
    image_filename = os.path.basename(image_path)

    with open(image_path, "rb") as image_file:
        response = client.post(
            "/expression",
            params={"feeling": "sad"},
            files={"file": (image_filename, image_file, "image/jpg")}
        )

    assert response.json()['recognize'] in feelings

def test_imitation_get_photo(client):
    feeling = random.sample(feelings, 1)[0]
    response = client.get(
        "/imitation/photo",
        params={"feeling": feeling}
    )

    assert response.json()['feeling'] == feeling
    assert response.json()['photo_url'].startswith("https://storage.googleapis.com/vici-smiler/")
    assert response.json()['photo_url'].endswith(".jpg")

def test_word_get_photo(client):
    response = client.get(
        "/word"
    )

    assert response.json()['answer'] in feelings
    assert response.json()['feeling_list'] == feelings
    assert response.json()['photo_url'].startswith("https://storage.googleapis.com/vici-smiler/")
    assert response.json()['photo_url'].endswith(".jpg")

pytest.main()