class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.stringEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida")
    @staticmethod
    def stringEhValida(url):
        if url:
            return True
        else:
            return False
    def retornaMoedas(self):
        buscaMoedaOrigem  = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[inicioSubstringMoedaOrigem : finalSubstringMoedaOrigem]
        if moedaOrigem == "moedadestino":
            moedaOrigem = self.verificaMoedaOrigem(buscaMoedaOrigem)

        inicioSubstringMoedaDestino = self.encontraIndiceInicioSubstring(buscaMoedaDestino)
        finalSubstringMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[inicioSubstringMoedaDestino:]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicioSubstring(self, moedaOuValor):
        return self.url.find(moedaOuValor) + len(moedaOuValor) + 1

    def verificaMoedaOrigem(self, buscaMoedaOrigem):
        self.url = self.url.replace("moedadestino", "real", 1)
        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        return self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

    def retornaValor(self):
        buscaValor = "Valor".lower()
        inicioSubstringValor = self.encontraIndiceInicioSubstring(buscaValor)
        valor = self.url[inicioSubstringValor:]
        return valor
