from ClassePessoa import Pessoa


class Militar(Pessoa):
    def __init__(self, nome, altura, peso):
        super().__init__(nome, altura, peso)
        if 'colete' in self.mochila:
            self.resistencia_de_dano = 1 + self.mochila['colete']
        else:
            self.resistencia_de_dano = 1

    def mostrar_mochila(self):
        print("========================")
        for k, v in self.mochila.items():
            print(f" {k}: {v}")
        print("========================")


if __name__ == "__main__":
    eu = Militar("Guilherme", "180cm", 86)
    while True:
        print("=========PERÍCIAS=========             =========ATRIBUTOS=========                   \n"
              f"|  Luta: {eu.pericias['luta']}              |             |  Força: {eu.atributos['força']}               |\n"
              f"|  Atletismo: {eu.pericias['atletismo']}          |             |  Agilidade:  {eu.atributos['agilidade']}          |\n"
              f"|  Investigação: {eu.pericias['investigação']}       |             |  Vontade:  {eu.atributos['vontade']}            |\n"
              f"|  Tecnologia: {eu.pericias['tecnologia']}         |             |  Vigor:  {eu.atributos['vigor']}              |\n"
              f"|  Mira: {eu.pericias['mira']}              |             |  Inteligência:  {eu.atributos['inteligência']}       |\n"
              f"|  Furtividade: {eu.pericias['furtividade']}        |             =========ATRIBUTOS=========\n"
              f"|  Resistência: {eu.pericias['resistência']}        |\n"
              f"|  Lábia: {eu.pericias['lábia']}              |             ====================================\n"
              f"|  Persuasão: {eu.pericias['persuasão']}          |             |  (1) Dano de Vida                |\n"
              "=========PERÍCIAS=========             |  (2) Dano de Sanidade            |\n"
              , end='')
        print("==========================             |  (3) Gastar PE                   |\n"
              f"|  Vida: {eu.vida}/60           |             |  (4) Dado                        |\n"
              f"|  Sanidade: {eu.sanidade}/42       |             |  (5) Mostrar Mochiila            |\n"
              f"|  PE: {eu.PE}/8               |             |  (6) Recuperar Vida              |\n"
              "==========================             |  (7) Recuperar Sanidade          |\n"
              "                                       |  (8) Recuperar PE                |\n"
              "                                       |  (9) Resetar Vida/Sanidade/PE    |\n"
              "                                       ===================================="
              )
        entrada = input("\n \t\tNúmero aqui: ")
        if len(entrada) != 1:
            print("Por favor entra apenas com 1 número:")
            continue

        if entrada == '1':
            dano = int(input("Entra com o dano aqui: "))
            if dano > eu.resistencia_de_dano:
                eu.vida -= dano - eu.resistencia_de_dano
        elif entrada == '2':
            dano = int(input("Entra com o dano aqui: "))
            eu.sanidade -= dano
        elif entrada == '3':
            dano = int(input("Quanto gastou de PE "))
            eu.sanidade -= dano
        elif entrada == '4':
            eu.dados()
        elif entrada == '5':
            eu.mostrar_mochila()
        elif entrada == '6':
            dano = int(input("Quanto de vida recuperou: "))
            eu.vida += dano
        elif entrada == '7':
            dano = int(input("Quanto de sanidade recuperou: "))
            eu.sanidade += dano
        elif entrada == '8':
            dano = int(input("Quanto de PE recuperou: "))
            eu.PE += dano
        elif entrada == '9':
            eu.vida = 60
            eu.sanidade = 42
            eu.PE = 8

        print("\n\n\n")
