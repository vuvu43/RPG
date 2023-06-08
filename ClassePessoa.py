import json
import random


class Pessoa:
    def __init__(self, nome, altura, peso):
        utilidades = json.load(open(r"UTILIDADES.json"))

        self._nome = nome
        self._altura = altura
        self._peso = peso
        self.pericias = self._ler_pericia()
        self.atributos = self._ler_atributos()
        self.mochila = self._ler_mochila()

        self._vida_maxima = utilidades['vida_maxima']
        self._vida = utilidades['vida']
        self._sanidade_maxima = utilidades['sanidade_maxima']
        self._sanidade = utilidades['sanidade']
        self._PE_maximo = utilidades['PE_maximo']
        self._PE = utilidades['PE']

    def modificar_pericia(self, pericia: str, novo_valor: int):
        if pericia not in self.pericias:
            print("A perícia digitada não existe.")
            return

        with open("PERICIAS.json") as file:
            pericias_recuperadas = json.load(file)

        pericias_recuperadas[pericia] = novo_valor

        with open("PERICIAS.json", 'w') as arquivo:
            json.dump(pericias_recuperadas, arquivo)

        self.pericias[pericia] = novo_valor

    def modificar_atributo(self, atributo: str, novo_valor: int):
        if atributo not in self.atributos:
            print("O Atributo digitado não existe.")
            return

        with open("ATRIBUTOS.json") as file:
            atributos_recuperados = json.load(file)

        atributos_recuperados[atributo] = novo_valor

        with open("ATRIBUTOS.json", 'w') as arquivo:
            json.dump(atributos_recuperados, arquivo)

        self.atributos[atributo] = novo_valor

    def modificar_mochila(self, item: str, novo_valor):
        if item not in self.mochila:
            print("O item digitado não existe.")
            return

        with open("MOCHILA.json") as file:
            mochila_recuperada = json.load(file)

        mochila_recuperada[item] = novo_valor

        with open("MOCHILA.json", 'w') as arquivo:
            json.dump(mochila_recuperada, arquivo)

        self.mochila[item] = novo_valor

    @staticmethod
    def _ler_pericia():
        with open(r'PERICIAS.json', "r") as file:
            return json.load(file)

    @staticmethod
    def _ler_mochila():
        with open(r'MOCHILA.json', "r") as file:
            return json.load(file)

    @staticmethod
    def _ler_atributos():
        with open(r'ATRIBUTOS.json', "r") as file:
            return json.load(file)

    @staticmethod
    def dados():
        dice = input('(1) D4\n'
                     '(2) D6\n'
                     '(3) D8\n'
                     '(4) D12\n'
                     '(5) D20\n').split()
        result = []
        for i in dice:
            if i == '1':
                x = random.randint(1, 4)
                result.append(x)
            elif i == '2':
                x = random.randint(1, 6)
                result.append(x)
            elif i == '3':
                x = random.randint(1, 8)
                result.append(x)
            elif i == '4':
                x = random.randint(1, 12)
                result.append(x)
            elif i == '5':
                x = random.randint(1, 20)
                result.append(x)
        result.sort()
        print(f'{result} -> {sum(result)}')

    @property
    def PE(self):
        return self._PE

    @PE.setter
    def PE(self, novo_PE):
        if novo_PE > self._PE_maximo:
            self._PE = self._PE_maximo
            return

        self._PE = novo_PE

        with open("UTILIDADES.json") as f:
            util = json.load(f)
            util['PE'] = novo_PE

        with open("UTILIDADES.json", "w") as f:
            json.dump(util, f)

    @property
    def sanidade(self):
        return self._sanidade

    @sanidade.setter
    def sanidade(self, nova_sanidade):
        if nova_sanidade > self._sanidade_maxima:
            self._sanidade = self._sanidade_maxima
            return

        self._sanidade = nova_sanidade

        with open("UTILIDADES.json") as f:
            util = json.load(f)
            util['sanidade'] = nova_sanidade

        with open("UTILIDADES.json", "w") as f:
            json.dump(util, f)

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, nova_vida):
        if nova_vida > self._vida_maxima:
            self._vida = self._vida_maxima
            return

        self._vida = nova_vida

        with open("UTILIDADES.json") as f:
            util = json.load(f)
            util['vida'] = nova_vida

        with open("UTILIDADES.json", "w") as f:
            json.dump(util, f)
