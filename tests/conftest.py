import pytest
import json


def load_json_file(name: str):
    with open(f"tests/mocks/{name}.json", "r") as f:
        return json.loads(f.read())


@pytest.fixture(scope="module")
def payment_result():
    return load_json_file("payment_result")
