# TODO: A cada 100 pessoas que visualizam o anúncio 12 clicam nele.

# TODO: A cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.

# TODO: A cada compartilhamento nas redes sociais gera 40 novas visualizações.

# TODO: 30 pessoas visualizam o anúncio original (não compartilhado) a cada 
# R$ 1,00 investido.

# TODO: O mesmo anúncio é compartilhado no máximo 4 vezes em sequência
#       (1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 
#        3ª pessoa -> compartilha -> 4ª pessoa)

def calculador_vizualiza(valor_pago):
    # TODO: Condições que foram pedidas no desafio
    # A cada R$1,00 gera 30 pessoas 
    if (valor_pago == 1.00):
        pessoa_inicial = 30
    elif (valor_pago > 1.00):
        pessoa_inicial = valor_pago * 30
    
    # TODO: Será gerado 12% de cliques pelo total de pessoas 
    # investidas iniciais
    if (pessoa_inicial < 100):
        clicar_Anuncio = pessoa_inicial * 0.12
    elif (pessoa_inicial > 100):
        clicar_Anuncio = pessoa_inicial * 0.12

    # TODO: Temos um compartilhamento máximo de 4 vezes seguidas
    # por anúncio, logo pode variar de 0 a 4
    if (clicar_Anuncio < 20):
        compartilha = int((clicar_Anuncio * 3) / 20)
        if (compartilha >= 5):
            pessoa_nova = 4 * 40
            total_compartilha = 4
        elif(compartilha < 5):
            pessoa_nova = compartilha * 40
            total_compartilha = compartilha
    elif (clicar_Anuncio == 20):
        compartilha = 3
    elif (clicar_Anuncio > 20):
        compartilha = (clicar_Anuncio * 3) / 20
        if (compartilha >= 5):
            pessoa_nova = 4 * 40
            total_compartilha = 4
        elif(compartilha < 5):
            pessoa_nova = compartilha * 40
            total_compartilha = compartilha

    # TODO: Soma pessoas investidas inicialmente e as pessoas que foram
    # alcançadas através das condições de cliques e compartilhamentos
    total_pessoas = pessoa_inicial + pessoa_nova

    # TODO: Mostra o valor invenstido e o total de visualização
    print(f'''
        Valor investido: R${valor_pago:.2f}   
        Total de visualizações aproximado: {int(total_pessoas)} pessoas                  
    ''')
    # TODO: Valores abaixo servem para visualização personalizada
    # Comartilamentos: {float(total_compartilha):.0f}
    # Pessoas Iniciais: {int(pessoa_inicial)}
    # Pessoas Novas: {int(pessoa_nova)}
    # Cliques: {int(clicar_Anuncio)}

# TODO: Insere o valor que será investido
valor_investido = float(input("Qual o valor incial invenstido em R$:"))

# TODO: Chama a função criada
calculador_vizualiza(valor_investido)
