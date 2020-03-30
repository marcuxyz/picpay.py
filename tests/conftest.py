import pytest
from tests.util import loadmock


@pytest.fixture(scope="module")
def payment_result():
    return loadmock("payment_result.json")


@pytest.fixture(scope="module")
def get_status_result():
    return {
        "referenceId": "11111",
        "status": "refunded",
        "authorizationId": "5c8e4c711c7e4c8d21b1",
    }


@pytest.fixture(scope="module")
def get_cancel_payment_result():
    return loadmock("cancel/cancel_result.json")
