from unittest import mock

import pytest

from picpay import Picpay
from picpay.__version__ import __version__


def test_version():
    assert __version__ == "1.1.1"


@mock.patch("picpay.picpay.Downloader")
def test_payment(mock_downloader, payment_result, snapshot):
    data_mock = {
        "referenceId": "4878711",
        "callbackUrl": "http://www.minhaloja.com.br/callback",
        "returnUrl": "http://www.minhaloja.com.br/cliente/pedido/4878711",
        "value": 375.25,
        "expiresAt": "2022-05-01T16:00:00-03:00",
        "buyer": {
            "firstName": "Bugs",
            "lastName": "Bunny",
            "document": "123.456.789-10",
            "email": "bugs.bunny@warnerbros.com",
            "phone": "+55 71 12345-6789",
        },
    }
    token = "some things..."

    mock_downloader.return_value.post.return_value = mock.Mock(json=payment_result)

    # get payment...
    picpay = Picpay(token)
    response = picpay.payment(data_mock)

    snapshot.assert_match(response.json)


@mock.patch("picpay.picpay.Downloader")
def test_get_status(mock_downloader, get_status_result, snapshot):
    referenceId = "11111"
    token = "some things..."

    mock_downloader.return_value.get.return_value = mock.Mock(json=get_status_result)

    # get status of payment...
    picpay = Picpay(token)
    response = picpay.get_status(referenceId)

    snapshot.assert_match(response.json)


@mock.patch("picpay.picpay.Downloader")
def test_cancel_payment(mock_downloader, get_cancel_payment_result, snapshot):
    mock_downloader.return_value.post.return_value = mock.Mock(
        json=get_cancel_payment_result
    )
    picpay = Picpay("some things...")
    response = picpay.cancel_payment("102030", "5c8e4c711c7e4c8d21b1")
    snapshot.assert_match(response.json)


@pytest.mark.asyncio
@mock.patch("picpay.picpay.Downloader", new_callable=mock.AsyncMock)
async def test_cancel_payment_async(
    mock_downloader, get_cancel_payment_result, snapshot
):
    downloader = mock_downloader.return_value
    downloader.post_async.return_value = mock.AsyncMock(json=get_cancel_payment_result)
    picpay = Picpay("some things...")
    picpay.downloader = downloader
    response = await picpay.cancel_payment_async("102030", "5c8e4c711c7e4c8d21b1")
    snapshot.assert_match(response.json)
