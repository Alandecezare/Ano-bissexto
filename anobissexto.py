# Solicita ao usuário que insira o ano desejado
ano = int(input("Por favor, insira o ano desejado: "))

# Verifica se o ano é bissexto de acordo com as regras do calendário gregoriano
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    # Se o ano for bissexto, imprime a explicação correspondente
    print(f"O ano {ano} é bissexto, pois é divisível por 4, exceto por ser divisível por 100, a menos que seja divisível por 400. Ele possui 366 dias.")
else:
    # Se o ano não for bissexto, imprime a explicação correspondente
    print(f"O ano {ano} não é bissexto, pois não segue as regras do calendário gregoriano. Ele possui 365 dias.")