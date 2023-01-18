# Modulo 1 #
# Automação de atendimento. #
# Autor:    João Carlos Agra dos Santos #
#           Angelica Monteiro Correa
#           Sheila 
#           Letícia de Sousa Ferreira
#           Raquel Reiner Tavares
#
# Fale Comigo. #
# Atendimento automatizado de dúvidas. #
'''
def sair (op):
    if op == 0:
        print("Agradecemos sua visita, volte sempre.")
        exit()   
    
    return print("Opção inválida. Digite uma opção válica.")'''

print()
print("-" * 40)
print()
print("Bem vindo a Bendito Tour.")
print("Sua empresa de viagens que é a glória.")
print()
print("-" * 40)
print()

op = 4

while op == 4:

            
    if op == 4:
        print("Olá! Eu sou Benedito. Seu atendente virtual.")
        print("Estou aqui especialmente para atender você. Em que posso ajudar?")
        print("Digite a opção desejada: ")
        print("1 - Reservas")
        print("2 - Comercial")
        print("3 - Financeiro")
        print("0 - Sair")

        op = int(input())

        if op == 0:
            print("Agradecemos sua visita, volte sempre.")
            exit()
        
        if op == 1:
            print()
            print("RESERVAS")
            print()
            print("Que legal! Quer saber sobre nossas reservas. Escolha uma opção que eu te ajudarei.")
            print("Digite a opção desejada: ")
            print("1 - Hospedagens disponíveis ")
            print("2 - Como fazer sua reserva")
            print("3 - Como cancelar sua reserva")
            print("4 - Voltar")

            op = int(input())

            if op == 1:
                print()
                print("HOSPEDAGENS DISPONÍVEIS")
                print()
                print("Vai conhecer agora os lugares mais bonitos do Brasil.")
                print("Digite a opção desejada: ")
                print("1 - Rio de Janeiro")
                print("2 - Porto Seguro")
                print("3 - Natal")
                print("4 - Voltar")

                op = int(input())

                if op == 1:
                    print()
                    print("Gamboa Rio Hotel")
                    print("1 - Diária a partir de R$ 100,00")
                    print("4 - Voltar")

                    op = int(input())

                    if op == 1:
                        print()
                        print("https://bit.ly/RioHotel")
                        print("4 - Voltar")
                        print()
                        op = int(input())

                elif op == 2:
                    print()
                    print("Hotel Fenix")
                    print("1 - Diária a partir de R$ 145,00")
                    print("4 - Voltar")

                    op = int(input())

                    if op == 1:
                        print()
                        print("https://bit.ly/HotelFenix")
                        print("4 - Voltar")
                        print()
                        op = int(input())



                elif op == 3:
                    print()
                    print("Yak Beach Hotel")
                    print("1 - Diária a partir de R$ 192,00")
                    print("4 - Voltar")

                    op = int(input())

                    if op == 1:
                        print()
                        print("https://bit.ly/yyyyyyyyy")
                        print("4 - Voltar")
                        print()
                        op = int(input())


            elif op == 2:
                print()
                print("COMO FAZER SUA RESERVA")
                print("Não tem nenhum mistério. Veja como é fácil:")
                print("Digite a opção desejada: ")
                print("1 - Ligue para o telefone (XX)XXX-XXXXX e faça já sua reserva")
                print("4 - Voltar")
                print()
                op = int(input())


            elif op == 3:
                print()
                print("COMO CANCELAR SUA RESERVA")
                print("Não vai poder viajar agora? Que pena.")
                print("Mas estaremos de braços abertos para próxima oportunidade.")
                print("Digite a opção desejada:")
                print("1 - Ligue para o telefone (XX) XXX-XXXXX e faça o cancelamento de sua reserva.")
                print("4 - Voltar")
                print()
                op = int(input())


        elif op == 2:
            print()
            print("COMERCIAL")
            print("Muito bem. Agora me indique o que precisa saber.")
            print("Digite a opção desejada:")
            print("1 - Formas de pagamento ")
            print("2 - Pacotes promocionais")
            print("4 - Voltar")

            op = int(input())

            if op == 1:
                print()
                print("FORMAS DE PAGAMENTO")
                print("Com essa molezinha, seu sonho de viagem fica mais real.")
                print("1 - À vista")
                print("2 - PIX")
                print("3 - Cartão de crédito")
                print("4 - Voltar")

                op = int(input())

                if op == 1:
                    print()
                    print("1 - Com desconto de 10%")
                    print("4 - voltar")

                    op = int(input())

                    if op == 1:
                        print()
                        print("https://bit.ly/yyyyyyyyy")
                        print("4 - Voltal")

                        op = int(input())

                elif op == 2:
                    print()
                    print("1 - Com desconto de 10%")
                    print("4 - Voltar")

                    op = int(input())

                    if op == 1:
                        print()
                        print("https://bit.ly/yyyyyyyyy")
                        print("4 - Voltal")

                        op = int(input())

                        if op == 1:
                            print()
                            print("https://bit.ly/yyyyyyyyy")
                            print("4 - Voltal")
                            op = int(input())

                elif op == 3:
                    print()
                    print("1 - Parcelado em até 5 vezes")
                    print("4 - Voltar")

                    op = int(input())

                    if op == 1:
                        print()
                        print("https://bit.ly/yyyyyyyyy")
                        print("4 - Voltal")

                        op = int(input())

        elif op == 2:
            print()
            print("PACOTES PROMOCIONAIS")
            print("Os melhores preços estão aqui.")
            print("Digite a opção desejada:")
            print("1 - Rio de Janeiro")
            print("2 - Buenos Aires")
            print("3 - Outras Ofertas")
            print("4 - Voltar")

            op = int(input())

            if op == 1:
                print()
                print("1 - Voo para o Rio de Janeiro ida e volta a partir de R$ 640,00 (Consulte condições)")
                print("4 - Voltar")

                op = int(input())

            elif op == 2:
                print()
                print("1 - Voo para Buenos Aires ida e volta a partir de R$ 1.740,00 (Consulte condiçoes)")
                print("4 - Voltar")

                op = int(input())

                if op == 1:
                    print()
                    print("Link: https://bit.ly/xxxyyyy")
                    print("4 - Voltar")

                    op = int(input())

            elif op == 3:
                print()
                print("1 - Ofertas de passagens a partir de R$ 299,00 (Consulte condiçoes")
                print("4 - Voltar")

                op = int(input())

                if op == 1:
                    print()
                    print("Link: https://bit.ly/xxxyyyy")
                    print("4 - Voltar")

                    op = int(input())

        elif op == 3:
            print()
            print("Financeiro")
            print("Bem vindo ao setor finacerio.")
            print("Digite a opção desejada:")
            print("1 - Código de barras")
            print("2 - Faturas vencidas")
            print("4 - Voltar")

            op = int(input())

            if op == 1:
                print("Link: https://bit.ly/boletoxxxxx")
                print("4 - Voltar")

                op = int(input())

            elif op == 2:
                print("Link: https://bit.ly/faturayyyyy")
                print("4 - Voltar")

                op = int(input())
            