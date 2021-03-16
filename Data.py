class Data:

    def dia_no_ano(dia, mes, ano):  #verifica os dias da data
        numero_de_dias = dia
        contador_meses = 1
        while contador_meses < mes:
            if contador_meses in (1, 3, 5, 7, 8, 10, 12):
                numero_de_dias += 31
            elif contador_meses in (4, 6, 9, 11):
                numero_de_dias += 30
            elif contador_meses == 2:
                numero_de_dias += 28
            contador_meses += 1
        return numero_de_dias

    def bissexto(ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) # verifica se o ano é bissexto ou não

    def validar_data(dia, mes, ano):  # verica se a data é válida
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1900:
            return False
        if mes in (4, 6, 9, 11) and dia == 31:
            return False
        if mes == 2 and dia >= 30:
            return False
        if mes == 2 and dia == 29 and not Data.bissexto(ano):
            return False
        return True

    def data_recente(data1, data2): # encontra a data mais recente
        # Separa os dados adequadamente e trata entradas mal-formadas.
        try:
            dia1, mes1, ano1 = [int(datando) for datando in data1.split("/")]
        except ValueError:
            raise ValueError('Data inválida: ' + data1)

        try:
            dia2, mes2, ano2 = [int(datador) for datador in data2.split("/")]
        except ValueError:
            raise ValueError('Data inválida: ' + data2)

        # Verifica se as datas entradas são válidas:
        if not Data.validar_data(dia1, mes1, ano1):
            raise ValueError('Data inválida: ' + data1)
        if not Data.validar_data(dia2, mes2, ano2):
            raise ValueError('Data inválida: ' + data2)

        # data mais recente
        if ano2 > ano1 or (ano2 == ano1 and (mes2 > mes1 or (mes2 == mes1 and dia2 > dia1))):
            return data2
        else:
            return data1

    def adicionar_um_dia(data1, data2): # adiciona um dia a uma data
        result = Data.data_recente(data1, data2)
        dia, mes, ano = [int(datando) for datando in result.split("/")]
        if dia == 31 and mes in (1, 3, 5, 7, 8, 10, 12):
            dia = 1
            if mes == 12:
                mes = 1
                ano += 1
            else:
                mes += 1
        elif dia == 30 and mes in (4, 6, 9, 11):
            dia = 1
            mes += 1
        elif dia == 29 and Data.bissexto(ano):
            dia = 1
            mes += 1
        elif dia == 28 and mes == 2:
            dia = 1
            mes += 1
        elif dia >= 1 and dia <= 29:
            dia += 1

        return dia, mes, ano

    def adicionando_dias(z, diasAdicionar): # adiciona dias a uma data fornecida

        dia, mes, ano = [int(datando) for datando in z.split("/")]
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        maxDay = meses[mes - 1]
        totalDays = dia + diasAdicionar

        while (totalDays > maxDay):

            mes = mes + 1
            if (mes == 13):
                ano = ano + 1
                mes = 1
            totalDays = totalDays - maxDay
            maxDay = meses[mes - 1]

        dia = totalDays
        return dia, mes,ano

    def diferenca_data(data1, data2): # calcula a diferença de dias entre duas datas

        # Separa os dados adequadamente e trata entradas mal-formadas.
        try:
            dia1, mes1, ano1 = [int(datando) for datando in data1.split("/")]
        except ValueError:
            raise ValueError('Data inválida: ' + data1)

        try:
            dia2, mes2, ano2 = [int(datador) for datador in data2.split("/")]
        except ValueError:
            raise ValueError('Data inválida: ' + data2)

        # Verifica se as datas entradas são válidas:
        if not Data.validar_data(dia1, mes1, ano1):
            raise ValueError('Data inválida: ' + data1)
        if not Data.validar_data(dia2, mes2, ano2):
            raise ValueError('Data inválida: ' + data2)

        # Inverte as datas se a data2 anteceder a data1.
        if ano2 < ano1 or (ano2 == ano1 and (mes2 < mes1 or (mes2 == mes1 and dia2 < dia1))):
            return -Data.diferenca_data(data2, data1)

        # Calcula o número de dias nos anos incompletos.
        dias_ano1 = Data.dia_no_ano(dia1, mes1, ano1)
        dias_ano2 = Data.dia_no_ano(dia2, mes2, ano2)

        # Calcula o número de dias totais, considerando os anos incompletos e anos completos de 365 dias.
        dias_total = dias_ano2 - dias_ano1 + (ano2 - ano1) * 365

        # Considera anos começando em 01/03 para poder fazer a correção dos anos bissextos.
        ano1b = ano1
        if mes1 < 3:
            ano1b -= 1

        ano2b = ano2
        if mes2 < 3:
            ano2b -= 1

        # Soma os dias dos anos bissextos. São os divisíveis por 4 que ocorrem entre ano1b e ano2b.
        dias_total += int(ano2b / 4) - int(ano1b / 4)

        # Subtrai os dias dos anos bissextos que não existiram na etapa anterior. São os divisíveis por 100.
        dias_total -= int(ano2b / 100) - int(ano1b / 100)

        # Soma de volta os dias dos anos bissextos que foram removidos a mais na etapa anterior. São os divisíveis por 400.
        dias_total += int(ano2b / 400) - int(ano1b / 400)

        # Resultado da função.
        return dias_total

    ####### Início do programa. #######


x = input("Primeira data : ")
y = input("Segunda data : ")
diasAdicionar = int(input("Digite o número de dias que deseja adicionar a uma data :"))
z = input("Digite a data :")



diferenca = Data.diferenca_data(x, y) # diferença entre datas
dataRecente = Data.data_recente(x, y) # data mais recente
umDia = Data.adicionar_um_dia(x, y) # adiciona um dia a data mais recente
diasAdicionados = Data.adicionando_dias(z, diasAdicionar) # adiciona dias a uma data fornecida

# Mostra o resultado.
print("Diferença entre datas : ", diferenca,"dias")
print("Data mais recente :", dataRecente)
print("Um dia após a data mais recente :", umDia)
print("Dias somados a data digitada :", diasAdicionados)

