from unittest import mock
from python_picpay import Picpay, __version__


def test_version():
    assert __version__ == "1.0.0"


@mock.patch("python_picpay.Downloader")
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

    mock_downloader.return_value.post.return_value = mock.Mock(result=payment_result)

    # get payment...
    picpay = Picpay(token)
    response = picpay.payment(data_mock)

    snapshot.assert_match(response.result)
