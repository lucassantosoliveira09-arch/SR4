class JogadorFutebol:
    def __init__(self, nome, apelido, posicao, titulos_principais, frase_impacto):
        self.nome = nome
        self.apelido = apelido
        self.posicao = posicao
        self.titulos = titulos_principais
        self.frase = frase_impacto

    def exibir_ficha(self):
        print(f"{'='*30}")
        print(f"FICHA TÉCNICA: {self.nome.upper()}")
        print(f"{'='*30}")
        print(f"Apelido: {self.apelido}")
        print(f"Posição: {self.posicao}")
        print(f"Principais Títulos: {', '.join(self.titulos)}")
        print(f"\nFrase de Efeito: \"{self.frase}\"")
        print(f"{'='*30}")

# Criando a instância do Sergio Ramos
sergio_ramos = JogadorFutebol(
    nome="Sergio Ramos García",
    apelido="El Capitán / Cuqui",
    posicao="Zagueiro Central",
    titulos_principais=["Copa do Mundo", "4x Champions League", "2x Eurocopa"],
    frase_impacto="O caráter é algo que se cultiva, não é algo com que se nasce."
)

# Executando a exibição
if __name__ == "__main__":
    sergio_ramos.exibir_ficha()