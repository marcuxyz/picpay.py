import pytest
import json


def load_json_file(name: str):
    with open(f"tests/mocks/{name}.json", "r") as f:
        return json.loads(f.read())


@pytest.fixture(scope="module")
def payment_result():
    return load_json_file("payment_result")


@pytest.fixture(scope="module")
def get_status_result():
    return {
        "referenceId": "11111",
        "status": "refunded",
        "authorizationId": "5c8e4c711c7e4c8d21b1",
    }


@pytest.fixture(scope="module")
def get_cancel_payment_result():
    return {"message": "Transação já foi cancelada"}
