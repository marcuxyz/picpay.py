[![Build Status](https://travis-ci.org/MarcusMann/python-picpay.svg?branch=master)](https://travis-ci.org/MarcusMann/python-picpay) ![GitHub](https://img.shields.io/github/license/marcusmann/python-picpay) ![GitHub top language](https://img.shields.io/github/languages/top/marcusmann/python-picpay) ![Coveralls github branch](https://img.shields.io/coveralls/github/marcusmann/python-picpay/master) ![GitHub All Releases](https://img.shields.io/github/downloads/marcusmann/python-picpay/total)
 ![GitHub issues](https://img.shields.io/github/issues/marcusmann/python-picpay)

# Python Picpay

**Python-Picpay** é um package (pacote) que integra bem com a api do [picpay](https://ecommerce.picpay.com/doc/). Com este pacote, podemos criar facilmente pagamentos, cancelá-los e sermos notificados quando houver uma mudança no status do pagamento.

## Instalação
Para instalar o python-picpay é muito fácil, pois, ele está localizado no [Pypi](https://pypi.org/project/python-picpay/).  Para instalar você pode executar o seguinte comando em seu terminal:

Para instalar você pode usar o comando em seu terminal:

```bash
$ pip install python-picpay
```

## Como usar
Antes de começar, você deve importar a class `Picpay` veja:
```python
from python_picpay import Picpay
```

Agora, você pode compor os dados do envio do pagamento, veja:

```python
payment_data = {
	"referenceId": "21144", # código do produto
	"callbackUrl": "https://seusite.com.br/callback",
	"returnUrl": "https://spacedevs.com.br/cliente/pedido/21144", 
	"value": 99.90, # preço do produto
	"expiresAt": "2022-05-01T16:00:00-03:00",
	"buyer": {
		"firstName": "Jose", # primeiro nome do comprador
		"lastName": "Santos", # sobrenome do comprador
		"document": "182.255.879-55", # cpf do comprador
		"email": "email_do_comprador@email.com",
		"phone": "+55 71 91111-1111",
	},
}
```
Atenção: Para entender melhor o que cada parâmetro desse significa, clique [aqui](https://ecommerce.picpay.com/doc/#tag/Requisicao-de-Pagamento) para ver a documentação oficial do picpay.

Logo em seguida crie um token, este token é necessário para que a picpay saiba que você é realmente você. Para obter o token, acesse sua conta de lojista.

https://lojista.picpay.com/ecommerce-token

```python
token = "seu_token"
```
E então, crie o pagamento...

```
picpay = Picpay(token)
response = picpay.payment(payment_data)
```
Você pode ver a resposta da requisição dando um print no response:

```python
print(response)`
```


## Testando a biblioteca
Para testar a biblioteca, dentro do mesmo diretório do projeto execute o comando:
```bash
$ make test
```

## Screenshots

### Pagamento realizado com sucesso

![paid](https://raw.githubusercontent.com/MarcusMann/python-picpay/master/prints/approved.png)

### Lista de vendas

![payments list](https://raw.githubusercontent.com/MarcusMann/python-picpay/master/prints/picpay-payment-list.png)

### Estorno da venda
![refound](https://raw.githubusercontent.com/MarcusMann/python-picpay/master/prints/refound.jpg)
