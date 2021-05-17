class Cadastro():
    
    def __init__(self, nome_anuncio, cliente, dia_inicio, 
                       mes_inicio, ano_inicio,dia_fim, mes_fim, 
                       ano_fim, valor_diario):
        
        self.nome_anuncio = nome_anuncio
        self._cliente = cliente
        self._dia_inicio = dia_inicio
        self._mes_inicio = mes_inicio
        self._ano_inicio = ano_inicio
        self._dia_fim = dia_fim
        self._mes_fim = mes_fim
        self._ano_fim = ano_fim
        self._valor_diario = valor_diario


    @property
    def nome_anuncio(self):
        return self._nome_anuncio

    @nome_anuncio.setter
    def nome_anuncio(self, nome_anuncio):
        self._nome_anuncio = nome_anuncio

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def dia_inicio(self):
        return self._dia_inicio

    @dia_inicio.setter
    def dia_inicio(self, dia_inicio):
        self._dia_inicio = dia_inicio
    
    @property
    def mes_inicio(self):
        return self._mes_inicio

    @mes_inicio.setter
    def mes_inicio(self, mes_inicio):
        self._mes_inicio = mes_inicio
    
    @property
    def ano_inicio(self):
        return self._ano_inicio

    @ano_inicio.setter
    def ano_inicio(self, ano_inicio):
        self._ano_inicio = ano_inicio
    
    @property
    def dia_fim(self):
        return self._dia_fim

    @dia_fim.setter
    def dia_fim(self, dia_fim):
        self._dia_fim = dia_fim
    
    @property
    def mes_fim(self):
        return self._mes_fim

    @mes_fim.setter
    def mes_fim(self, mes_fim):
        self._mes_fim = mes_fim
    
    @property
    def ano_fim(self):
        return self._ano_fim

    @ano_fim.setter
    def ano_fim(self, ano_fim):
        self._ano_fim = ano_fim

    @property
    def valor_diario(self):
        return self._valor_diario

    @valor_diario.setter
    def valor_diario(self, valor_diario):
        self._valor_diario = valor_diario
    
    @property
    def anuncio(self):
        return self.anuncio

    @anuncio.setter
    def anuncio(self, anuncio):
        self._anuncio = anuncio
    
    @property
    def cadastro_list(self):
        return self._cadastro_list

    @cadastro_list.setter
    def cadastro_list(self, cadastro_list):
        self._cadastro_list = cadastro_list
    

# pessoa = Pessoa('Miguel', 30, 50)
# print(pessoa.__dict__) # valores iniciais
# Cadastro.data_inicio = 'Teste'
# Cadastro.get_nome_anuncio = 'teste'
# pessoa.idade = 20
# pessoa.salario = 500
# print(Cadastro.data_inicio)
# print(pessoa.idade)
# print(pessoa.salario)


# def main():
#     nome_anuncio = 'teste1'
#     # Cadastro.cliente = 'teste2'
#     # Cadastro.dia_inicio = 'teste3'
#     # Cadastro.mes_inicio = 'teste4'
#     # Cadastro.ano_inicio = 'teste5'
#     # Cadastro.dia_fim = 'teste6'
#     # Cadastro.mes_fim = 'teste7'
#     # Cadastro.ano_fim = 'teste8'
#     # Cadastro.valor_diario = 'teste11'

#     anuncio = []
#     cadastro_list = ["Anuncio"]
    
#     # , "cliente","dia inicio", "Mes inicio",
#     #                 "Ano inicio", "dia fim", "mes fim", "ano fim",
#     #                 "data fim", "data inicio","valor diario"

#     anuncio.append(list(Cadastro.nome_anuncio))

#                             # , Cadastro.cliente, 
#                             # Cadastro.dia_inicio, Cadastro.mes_inicio,
#                             # Cadastro.ano_inicio, Cadastro.dia_fim,
#                             # Cadastro.mes_fim, Cadastro.ano_fim,
#                             # Cadastro.valor_diario
    
#     lista_zip = str(list((zip(cadastro_list, anuncio))))

#     # for c, d in lista_zip:
#     #     print(c, " = ", d)

#     # teste_dias = list(dias_en)

#     for i, d in enumerate(list(zip(cadastro_list, anuncio))):
#         print(i+1, d[0], " = ", d[1])
    
#     # for pessoa in zip(anuncio,cadastro_list):
#     #     print(f'''{pessoa}''')

#     # for pessoa in anuncio:
#     #     print(f'''{pessoa.nome_anuncio}''')

#     # print([x for x in anuncio if type(x) == bytes])

# if __name__ == "__main__":
#     main()