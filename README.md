[![Build Status](https://travis-ci.org/MarcusMann/python-picpay.svg?branch=master)](https://travis-ci.org/MarcusMann/python-picpay) ![GitHub](https://img.shields.io/github/license/marcusmann/python-picpay) ![GitHub top language](https://img.shields.io/github/languages/top/marcusmann/python-picpay) [![Coverage Status](https://coveralls.io/repos/github/MarcusMann/python-picpay/badge.svg?branch=master)](https://coveralls.io/github/MarcusMann/python-picpay?branch=master) ![GitHub All Releases](https://img.shields.io/github/downloads/marcusmann/python-picpay/total)
 ![GitHub issues](https://img.shields.io/github/issues/marcusmann/python-picpay)

# Python Picpay

**Python-Picpay** é um package (pacote) que integra bem com a api do [picpay](https://ecommerce.picpay.com/doc/). Com este pacote, podemos criar facilmente pagamentos, cancelá-los e sermos notificados quando houver uma mudança no status do pagamento.

## Instalação
Para instalar o python-picpay é muito fácil, pois, ele está localizado no [Pypi](https://pypi.org/project/picpay/).  Para instalar você pode executar o seguinte comando em seu terminal:

```bash
$ pip install picpay
```

## Como usar
Para obter informações de como utilizar a lib, você pode ver a documentação clicando [aqui](https://mpereirassa.gitbook.io/picpay-py/).


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
