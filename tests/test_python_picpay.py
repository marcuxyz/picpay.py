from unittest import mock
from picpay import Picpay
from picpay.__version__ import __version__


def test_version():
    assert __version__ == "1.1.0"


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
    referenceId = "11111"
    authorizationId = "2ce49cu917a8ci10cn"

    token = "some things..."

    mock_downloader.return_value.post.return_value = mock.Mock(
        json=get_cancel_payment_result
    )

    # get cancel payment...
    picpay = Picpay(token)
    response = picpay.cancel_payment(referenceId, authorizationId)

    snapshot.assert_match(response.json)
