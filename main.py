# Aluno: Gabriel Silva Lima
# entrega da fase 2 da disciplina de Lógica e Programação de Computadores
# Pra este projeto, tentei ao máximo não utilizar bibliotecas externas, apenas as nativas do python
# repositório: https://github.com/gabriellimma/pucrs-wheater-data-calculator-phase-2
# link do colab:
import matplotlib.pyplot as plt


def abrir_arquivo(arquivo):
    """Função que abre um arquivo para leitura.

    Returns:
    os dados de um arquivo
   """
    arq = open(arquivo, 'r')
    return arq


def fechar_arquivo(arquivo):
    """Função que fecha um arquivo aberto.

    Returns:
    void
   """
    arquivo.close()


def transforma_dados_em_lista(path_arquivo):
    """Função que transforma os dados de um arquivo de CSV para em uma lista de tuplas,
    organizando e tipando corretamente os dados para análise.

    Returns:
    lista de tuplas
   """
    # abre o arquivo
    arquivo = abrir_arquivo(path_arquivo)
    # lê todas as linhas do arquivo e armazena em uma lista
    dados = arquivo.readlines()
    # remove a primeira linha do arquivo, que é o cabeçalho
    dados.remove(dados[0])
    # variável que vai receber um array de dados encontrados no arquivo
    data_set = []
    # para cada linha encontrada no arquivo
    for linha in dados:
        # transformamos cada linha em um array de strings, separando os valores pelo caractere ','
        valores = linha.split(',')
        # transformamos o array de strings em uma tupla de valores com todos os valores que precisamos para a análise
        tupla = ((valores[0]), float(valores[1]), float(valores[2]), float(valores[3]), float(valores[4]),
                 float(valores[5]), float(valores[6]), float(valores[7]))
        # adicionamos a tupla de valores ao array data_set
        data_set.append(tupla)
    # fecha o arquvo depois da leitura e de transformar os dados em uma lista de tuplas
    fechar_arquivo(arquivo)
    # retornamos o array de tuplas
    return data_set


def seleciona_dados_por_data(data_set, mes_inicio, ano_inicio, mes_fim, ano_fim):
    """Função que faz a seleção dos dados de uma lista de tuplas a partir de uma data início até uma data fim,
    organizando por datas e retornando um novo array de tuplas com os dados selecionados.

    Returns:
    lista de tuplas
   """
    data_selecionada = []

    for data in data_set:
        # se o ano encontrada na iteração for igual ao ano de início e o mes for maior ou igual ao mes de início
        # ou se o ano for maior que o ano de início e menor ou igual ao ano final
        # então pode ser uma data válida
        if (int(data[0][6:10]) == int(ano_inicio) and int(data[0][3:5]) >= int(mes_inicio)
            or int(data[0][6:10]) > int(ano_inicio)) and (int(data[0][6:10]) <= int(ano_fim)):
            # E se a o ano encontrado for igual ao ano final e a data encontrada for maior que o mes final,
            # a busca é encerrada
            if int(data[0][6:10]) == int(ano_fim) and int(data[0][3:5]) > int(mes_fim):
                break
            else:
                # enquanto a busca não é encerrada, adicionamos a data na lista de dados selecionados
                data_selecionada.append(data)
    # devolve a nova lista contendo os dados selecionados a partir do intervalo de datas
    return data_selecionada


def visualizar_dados_modo_texto(data_set):
    """Função que faz o output dos dados no terminal, de acordo com a seleção do usuário,
    a partir de uma data início até uma data fim, podendo ter as opções de mostrar
    todos os dados ou apenas os dados de precipitação, temperatura, umidade e vento.

    Returns:
    void
   """
    # entrada de dados do usuário
    mes_inicio = input("Digite o mês de início que deseja ver os dados (01 a 12): ")
    ano_inicio = input("Digite o ano de início que deseja ver os dados (1961 a 2016): ")
    mes_fim = input("Digite o mês de fim que deseja ver os dados (01 a 12): ")
    ano_fim = input("Digite o ano de fim que deseja ver os dados (1961 a 2016): ")

    # se o mês de início ou fim tiver apenas um caractere, adiciona um 0 a esquerda
    if len(mes_inicio) == 1:
        mes_inicio = '0' + mes_inicio
    if len(mes_fim) == 1:
        mes_fim = '0' + mes_fim

    # valida as datas inseridas, por exemplo, se o mês for maior que 12 ou menor que 1, ou se o ano for menor que 1961.
    if ((mes_inicio == '' or mes_fim == '' or ano_inicio == '' or ano_fim == ''
         or float(mes_inicio) > 12 or float(mes_fim) > 12 or float(mes_inicio) < 1 or float(mes_fim) < 1
         or float(ano_inicio) < 1961 or float(ano_fim) > 2016 or float(ano_inicio) > float(ano_fim))
            or float(mes_fim) < float(mes_inicio) and float(ano_fim) == float(ano_inicio)):
        print("Datas inválidas, valide se os dados foram inseridos corretamente")
        reiniciar = input("desja reinicar a operação? S/N\n")
        if reiniciar == 'S' or reiniciar == 's':
            # chama a função novamente caso seja selecionado reiniciar a operação
            visualizar_dados_modo_texto(data_set)
        else:
            print("Operação finalizada")
    else:
        # pergunta ao usuário quais dados deseja ver
        dados_selecionados = input("Quais dados deseja ver?\n1 - Todos\n2 - Precipitação"
                                   "\n3 - Temperatura\n4 - Umidade e vento\n")

        # seleciona os dados a partir de uma data início até uma data fim
        data_selecionada = seleciona_dados_por_data(data_set, mes_inicio, ano_inicio, mes_fim, ano_fim)
        dict_data_selecionada = []
        # transforma os dados em dicionário para facilitar a visualização
        for i in data_selecionada:
            dicio = {'data': i[0], 'precip': i[1], 'maxima': i[2], 'minima': i[3], 'horas_insol': i[4],
                     'temp_media': i[5], 'um_relativa': i[6], 'vel_vento': i[7]}
            dict_data_selecionada.append(dicio)

        if dados_selecionados == '1':
            # apresenta todos os dados
            # imprime o cabeçalho no formato de tabela
            cabecalho = ["data", "precip", "maxima", "minima", "horas_insol", "temp_media", "um_relativa", "vel_vento"]
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*cabecalho))
            # para cada linha de dados encontrados, imprime os valores no formato de tabela abaixo do cabeçalho
            for data in data_selecionada:
                print("{:<10} {:<10} {:<10} {:<10} {:<10}  {:<10}  {:<10}  {:<10}".format(*data))
        elif dados_selecionados == '2':
            # apresenta apenas os dados de precipitação
            # imprime o cabeçalho no formato de tabela
            cabecalho = ["data", "precip"]
            print("{:<10} {:<10}".format(*cabecalho))
            # para cada linha de dados encontrados, imprime os valores no formato de tabela abaixo do cabeçalho
            for data in dict_data_selecionada:
                print("{:<10} {:<10}".format(data['data'], data['precip']))
        elif dados_selecionados == '3':
            # apresenta apenas os dados de temperatura
            # imprime o cabeçalho no formato de tabela
            cabecalho = ["data", "maxima", "minima", "temp_media"]
            print("{:<10} {:<10} {:<10} {:<10}".format(*cabecalho))
            # para cada linha de dados encontrados, imprime os valores no formato de tabela abaixo do cabeçalho
            for data in dict_data_selecionada:
                print("{:<10} {:<10} {:<10} {:<10}".format(data['data'], data['maxima'], data['minima'],
                                                           data['temp_media']))
        elif dados_selecionados == '4':
            # apresenta apenas os dados de umidade e vento
            # imprime o cabeçalho no formato de tabela
            cabecalho = ["data", "um_relativa", "vel_vento"]
            print("{:<10} {:<10} {:<10}".format(*cabecalho))
            # para cada linha de dados encontrados, imprime os valores no formato de tabela abaixo do cabeçalho
            for data in dict_data_selecionada:
                print("{:<10} {:<10}  {:<10}".format(data['data'], data['um_relativa'], data['vel_vento']))
        else:
            print("Opção inválida")
            reiniciar = input("desja reinicar a operação? S/N\n")
            if reiniciar == 'S' or reiniciar == 's':
                # chama a função novamente caso seja selecionado reiniciar a operação
                visualizar_dados_modo_texto(data_set)
            else:
                print("Operação finalizada")


def mes_mais_chuvoso_do_ano(data_set, ano):
    """Função que retorna o mês mais chuvoso do ano informado em {ano}, de acordo com a precipitação total
    a partir da análise de todos osm eses daquele ano.

    Returns:
    Dicionário com o mês mais chuvoso de um ano
   """
    # array vazio para receber uma lista de dicionários
    dict_arr = []
    dict_arr_ano = []
    dict_arr_mes = []
    mes_mais_chuvoso = {'ano': 0, 'media_precipitacao': 0, 'mes': 0, 'precipitacao': 0, 'qtd_dias': 0}

    # cria um dicionário com a data e a precipitação
    for data in data_set:
        dicio = {'data': data[0], 'precipitacao': data[1]}
        dict_arr.append(dicio)

    # cria um dicionário com a data e a precipitação de acordo com o ano
    for i in dict_arr:
        if i['data'][6:10] == str(ano):
            dicio = {'data': i['data'], 'precipitacao': i['precipitacao']}
            dict_arr_ano.append(dicio)

    # cria um dicionário com a média de precipitação do mês
    for i in range(1, 13):
        precipitacao_mes = 0
        dias = 0
        # separa a precipitação do mes somando todas as precipitações do mês e dividindo pela quantidade de dias
        # do mesmo mês
        for j in dict_arr_ano:
            if j['data'][3:5] == str('%02d' % i):
                precipitacao_mes += j['precipitacao']
                dias += 1
        # só fazemos a média se a precipitação do mes for maior que 0
        if precipitacao_mes > 0:
            media_precipitacao = precipitacao_mes / dias
        # se não, mantemos a média como 0
        else:
            media_precipitacao = 0
        # no fim, montamos um dicionário com o mês, o ano, a precipitação total, a quantidade de dias e a média
        dicio = {'mes': i, 'ano': ano, 'precipitacao': precipitacao_mes, 'qtd_dias': dias,
                 'media_precipitacao': media_precipitacao}
        dict_arr_mes.append(dicio)

    # compara a precipitação mes a mes e retorna o mês mais chuvoso de acordo com a precipitação naquele ano
    for i in dict_arr_mes:
        if mes_mais_chuvoso['precipitacao'] < i['precipitacao']:
            mes_mais_chuvoso = i
    return mes_mais_chuvoso


def mes_mais_chuvoso(data_set):
    f"""Função que retorna o mês mais chuvoso de todos os anos, de acordo com a precipitação total,
    usando a função mes_mais_chuvoso_do_ano(data_set, ano) para fazer a comparação entre os anos. 

    Returns:
    Dicionário com o mês, ano e média de precipitação do mais chuvoso de todos os anos
   """
    # cria um dicionário que será populado com o mes, ano, e média de precipitação do mês mais chuvoso
    mes_mais_chuvoso_de_todos = {'mes': '00', 'ano': '00', 'media_precipitacao': 00}

    # compara a precipitação mes a mes e retorna o mês mais chuvoso de acordo com a precipitação de cada ano
    for i in range(1961, 2017):
        # compara ano a ano o mês mais chuvoso e retorna o com a maior precipitação
        if mes_mais_chuvoso_de_todos['media_precipitacao'] < mes_mais_chuvoso_do_ano(data_set, i)['media_precipitacao']:
            mes_mais_chuvoso_de_todos = mes_mais_chuvoso_do_ano(data_set, i)
    print(f'O mês mais chuvoso entre todos os anos foi o mês: {mes_mais_chuvoso_de_todos["mes"]} no ano de '
          f'{mes_mais_chuvoso_de_todos["ano"]}, com a precipitação mensal de de {mes_mais_chuvoso_de_todos["precipitacao"]}mm.')
    print(f'Dicionário: {mes_mais_chuvoso_de_todos}')
    return mes_mais_chuvoso_de_todos


def temperatura_minima_mes(data_set, mes=-1, mostrar_tabela=True):
    if mes == -1:
        mes = int(input("Digite o mês que deseja ver a média de temperatura mínima (01 a 12): "))
    is_mes_valido = False
    if mes < 1 or mes > 12:
        print("Mês inválido")
        reiniciar = input("desja reinicar a operação? S/N\n")
        if reiniciar == 'S' or reiniciar == 's':
            # chama a função novamente caso seja selecionado reiniciar a operação
            temperatura_minima_mes(data_set)
        else:
            print("Operação finalizada")
    else:
        is_mes_valido = True

    # selecionamos apenas a tupla contendo os dados dos anos de 01/2006 a 12/2016
    ultimos_anos = seleciona_dados_por_data(data_set, 1, 2006, 7, 2016)
    # array vazio para receber uma lista de tuplas como dicionários
    dict_arr = []
    # array vazio para receber a média de mês / ano de temperaturas mais frias
    dict_media_mes_ano = []

    # cria um dicionário com a data e a temperatura mínima de todos os meses
    for data in ultimos_anos:
        dicio = {'data': data[0], 'minima': data[3]}
        dict_arr.append(dicio)

    # cria variáveis para armazenar a média de temperatura mínima e um iterador
    media_temperatura_minima = 0
    iterador = 0
    # cria um dicionário com a média de temperatura mínima do mês
    for i in dict_arr:
        # faz a soma das temperaturas mínimas enquanto o mês for igual ao mês que queremos a média
        if i['data'][3:5] == str('%02d' % mes):
            media_temperatura_minima += i['minima']
            iterador += 1
            data = i['data']
        # quando o mês se torna diferente, calculamos a média e adicionamos ao array de médias
        if i['data'][3:5] != str('%02d' % mes) and media_temperatura_minima > 0 or i == dict_arr[-1]:
            if iterador > 0:
                media_temperatura_minima = media_temperatura_minima / iterador
                # montamos um dicionário com o mês, o ano e a média de temperatura mínima
                dicio = {'mes': mes, 'ano': data[6:10], 'media_temperatura_minima': media_temperatura_minima}
                # adicionamos a média ao array de médias
                dict_media_mes_ano.append(dicio)
                # zeramos as variáveis para fazer a média do próximo mês
                media_temperatura_minima = 0
                iterador = 0
    if is_mes_valido and mostrar_tabela:
        # imprime o cabeçalho no formato de tabela
        cabecalho = ["mes", "ano", "media_temperatura_minima"]
        print(f'Média de temperatura mínima do mês {mes} dos anos de 2006 a 2016')
        # para cada linha de dados encontrados, imprime os valores no formato de tabela abaixo do cabeçalho
        print("{:<10} {:<10} {:<10}".format(*cabecalho))
        for data in dict_media_mes_ano:
            print("{:<10} {:<10} {:<10}".format(data['mes'], data['ano'], data['media_temperatura_minima']))
    # retorna o array de médias
    return dict_media_mes_ano


def media_geral_temperatura_minima(data_set):
    """Função que faz a seleção dos dados de uma lista de tuplas a partir de uma data início até uma data fim,
    organizando por datas e retornando um novo array de tuplas com os dados selecionados.

    Returns:
    lista de tuplas
   """
    # recebe o mês via inout do usuário
    mes = int(input("Digite o mês que deseja ver a média de temperatura mínima (01 a 12): "))
    # valida o mês inserido
    if mes < 1 or mes > 12:
        print("Mês inválido")
        reiniciar = input("desja reinicar a operação? S/N\n")
        if reiniciar == 'S' or reiniciar == 's':
            # invoca a função novamente caso seja selecionado reiniciar a operação
            media_geral_temperatura_minima(data_set, mes)
        else:
            print("Operação finalizada")
    # se o mês for válido, calcula a média de temperatura mínima do mês e a média geral
    else:
        media_mensal = temperatura_minima_mes(data_set, mes, False)
        media_geral = 0
        for i in media_mensal:
            media_geral += i['media_temperatura_minima']
        print(
            f'Média geral de temperatura mínima do mês {mes} dos anos de 2006 a 2016 foi de: {media_geral / len(media_mensal)}')


def grafico_barras(data_set):
    """Função que constrói o gráfico de barras de acordo com o a temperatura mínima média
    dos últimos 11 anos a partir de 2006.

    Returns:
    void
   """
    mes = int(input("Digite o mês que deseja gerar o gráfico de barras com a média da temperatura mínima (01 a 12): "))
    if mes < 1 or mes > 12:
        print("Mês inválido")
        reiniciar = input("desja reinicar a operação? S/N\n")
        if reiniciar == 'S' or reiniciar == 's':
            # chama a função novamente caso seja selecionado reiniciar a operação
            media_geral_temperatura_minima(data_set)
        else:
            print("Operação finalizada")
    else:
        media_mensal = temperatura_minima_mes(data_set, mes, False)
        anos = []
        medias = []
        for i in media_mensal:
            anos.append(i['ano'])
            medias.append(i['media_temperatura_minima'])

        plt.bar(anos, medias)
        plt.xlabel('Ano')
        plt.ylabel('Temperatura mínima média')
        plt.title(f'Média de temperatura mínima do mês {mes} dos anos de 2006 a 2016')
        plt.show()


# inicialização dos dados
data_set = transforma_dados_em_lista('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv')

# Resposta para fase dois do projeto de lógica e programação de computadores A
# Visualização de dados em modo texto
print("----------------- INÍCIO Visualização de intervalo de dados em modo texto --------------------")
visualizar_dados_modo_texto(data_set)
print("------------------- FIM Visualização de intervalo de dados em modo texto -------------------\n")

# Resposta para fase dois do projeto de lógica e programação de computadores B
# Mês mais chuvoso de todos os anos
print("----------------------------------- INÍCIO Mês mais chuvoso ----------------------------------")
mes_mais_chuvoso(data_set)
print("------------------------------------- FIM Mês mais chuvoso -----------------------------------\n")


# Resposta para fase dois do projeto de lógica e programação de computadores C
# Média da temperatura mínima de um determinado mês
print("-------------------- INÍCIO Média da temperatura mínima de um determinado mês ----------------")
temperatura_minima_mes(data_set)
print("-------------------- FIM Média da temperatura mínima de um determinado mês -------------------\n")

# Resposta para fase dois do projeto de lógica e programação de computadores D
# Gráfico de barras
print("-------------------- INÍCIO Gráfico de barras -------------------")
grafico_barras(data_set)
print("-------------------- FIM Gráfico de barras -------------------\n")


# Resposta para fase dois do projeto de lógica e programação de computadores E
# Média da temperatura mínima de um determinado mês com sua média geral
print("---- INÍCIO Média geral da temperatura mínima de um determinado mês nos últimos 11 anos ----")
media_geral_temperatura_minima(data_set)
print("---- FIM Média geral da temperatura mínima de um determinado mês nos últimos 11 anos ----")
