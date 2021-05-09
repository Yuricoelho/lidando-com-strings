
from ExtratorArgumentosUrl import ExtratorArgumentosUrl
url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem, moedaDestino, valor)
url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem, moedaDestino, valor)


