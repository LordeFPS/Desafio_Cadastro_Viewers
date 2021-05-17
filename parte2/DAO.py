from datetime import datetime
import os     # importa uma opção para limpar a tela
import time   # importa opções de timer 
from cadastro import Cadastro
from string import Template
import itertools

def menu():
    print('''
    **********************
    ** 1 - Cadastrar    **
    ** 2 - Ver anúncios **
    ** 3 - Sair         **
    **********************
    ''')

# TODO: Função para achar a diferença de dias cadastrada
def diff_dias(data_inicio, data_fim = datetime.now, interval = "secs"):

    duration = data_fim - data_inicio
    duration_in_s = duration.total_seconds() 
    
    #Date and Time constants
    yr_ct = 365 * 24 * 60 * 60 #31536000
    day_ct = 24 * 60 * 60 		 #86400
    hour_ct = 60 * 60 				 #3600
    minute_ct = 60 
    
    def yrs():
      return divmod(duration_in_s, yr_ct)[0]

    def days():
      return divmod(duration_in_s, day_ct)[0]

    def hrs():
      return divmod(duration_in_s, hour_ct)[0]

    def mins():
      return divmod(duration_in_s, minute_ct)[0]

    def secs(): 
      return duration_in_s

    return {
        'yrs': int(yrs()),
        'days': int(days()),
        'hrs': int(hrs()),
        'mins': int(mins()),
        'secs': int(secs())
    }[interval]

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
Cliques: {int(clicar_Anuncio)}
Comartilamentos: {float(total_compartilha):.0f}
    ''')
    # TODO: Valores abaixo servem para visualização personalizada
    # Comartilamentos: {float(total_compartilha):.0f}
    # Pessoas Iniciais: {int(pessoa_inicial)}
    # Pessoas Novas: {int(pessoa_nova)}
    # Cliques: {int(clicar_Anuncio)}

# cria um  um procedimento que executa o código abaixo 
def limpa_tela_key(): 
    
    #time.sleep(tempo) # conseguimos fazer um temporizador de tela

    print("Pressione ENTER para continuar!")
    input()
    # com esse código conseguimos limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
def limpa_tela(tempo): 
    
    time.sleep(tempo) # conseguimos fazer um temporizador de tela

    # com esse código conseguimos limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')

def valida_data():
    while True:
        Cadastro.dia_inicio = int(input("Dia início: "))
        if (Cadastro.dia_inicio < 1 or Cadastro.dia_inicio > 31):
            print("Dia inválido.")
            continue
        else:
            break
    while True:
        Cadastro.mes_inicio = int(input("Mes início: "))
        if (Cadastro.mes_inicio < 1 or Cadastro.mes_inicio > 12):
            print("Mês inválido.")
            continue
        else:
            break
    while True:
        Cadastro.ano_inicio = int(input("Ano início: "))
        if(Cadastro.ano_inicio < 2021):
            print("Ano inválido.")
            continue
        else:
            break
    while True:
        Cadastro.dia_fim = int(input("Dia fim: "))
        if (Cadastro.dia_fim < 1 or Cadastro.dia_fim > 31):
            print("Dia inválido.")
            continue
        else:
            break
    while True:
        Cadastro.mes_fim = int(input("Mes fim: "))
        if (Cadastro.mes_inicio > Cadastro.mes_fim):
            print("Mês menor que mês inicial")
            continue
        elif (Cadastro.mes_fim < 1 or Cadastro.mes_fim > 12):
            print("Mês inválido.")
            continue
        else:
            break
    while True:
        Cadastro.ano_fim = int(input("Ano fim: "))
        if (Cadastro.ano_inicio > Cadastro.ano_fim):
            print("Ano menor que ano inicial")
        elif(Cadastro.ano_fim < 2021):
            print("Ano inválido.")
            continue
        else:
            break
    Cadastro.data_inicio = datetime(Cadastro.ano_inicio, 
                                    Cadastro.mes_inicio, 
                                    Cadastro.dia_inicio)
    Cadastro.data_fim = datetime(Cadastro.ano_fim, 
                                Cadastro.mes_fim, 
                                Cadastro.dia_fim)
    dias = diff_dias(Cadastro.data_inicio, Cadastro.data_fim, 'days')
    return dias

anuncio = []
cadastro_list = []
def listar_anuncio():
    data_inteira_inicio = Template("${dia_init}/${mes_init}/${ano_init}")
    dados_inicio = {
        "dia_init": Cadastro.dia_inicio,
        "mes_init": Cadastro.mes_inicio,
        "ano_init": Cadastro.ano_inicio
    }
    frase_inicio = data_inteira_inicio.substitute(dados_inicio)

    data_inteira_fim = Template("${dia_fim}/${mes_fim}/${ano_fim}")
    dados_fim = {
        "dia_fim": Cadastro.dia_fim,
        "mes_fim": Cadastro.mes_fim,
        "ano_fim": Cadastro.ano_fim
    }
    frase_fim = data_inteira_fim.substitute(dados_fim)

    valor_templ = Template("BRL ${valor_listar}")
    dados_valor = {
        "valor_listar": Cadastro.valor_diario
    }
    frase_valor = valor_templ.substitute(dados_valor)

    anuncio.append(Cadastro.nome_anuncio)
    cadastro_list.append("Anuncio")
    anuncio.append(Cadastro.cliente)
    cadastro_list.append("Cliente")
    anuncio.append(frase_inicio)
    cadastro_list.append("Data inicio")
    anuncio.append(frase_fim)
    cadastro_list.append("Data Final")
    anuncio.append(frase_valor)
    cadastro_list.append("valor diario")

    for i, d in enumerate(itertools.zip_longest(cadastro_list, list((anuncio)))):
        print(d[0], " = ", d[1])
