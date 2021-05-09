from ExtratorArgumentosUrl import ExtratorArgumentosUrl
import re
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

padrao = "[0-9]{4,5}-?[0-9]{4}"
texto = "Meu número para contato é 2633-5723"
retorno = re.search(padrao,texto)
print(retorno.group())


