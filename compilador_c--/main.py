#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AnalisadorLexico import AnalisadorLexico
from texttable import Texttable
import sys

def main(args):
    if(len(args) != 2):
        print("MODO DE EXECUCAO DO PROGRAMA: ")
        print("python3", "<main.py>", "<arquivo-codigo-fonte>")
        print("Obs: O <arquivo-codigo-fonte> deve conter o código em C--")
        return
    arquivo = open(args[1], 'r')
    linhas = arquivo.read().splitlines()
    linhas = preProcessamento(linhas)
    print(linhas)
    resultadoAnaliseLexica = AnalisadorLexico.main(linhas)

    tokens = resultadoAnaliseLexica[0]
    tabela = resultadoAnaliseLexica[1]
    dadosTokens = resultadoAnaliseLexica[2]
    errosLexicos = resultadoAnaliseLexica[3]

    imprimeTokens(dadosTokens)
    imprimeErros(errosLexicos)
    imprimeTabela(tabela)



def imprimeTokens(dadosTokens):
    for item in dadosTokens:
        print('Lexema: {:24} Linha: {:3}   Coluna: {:3}   Tipo do Token: {}'.format(item[0], item[1],
                                                                                    item[2], item[3]))

def imprimeErros(erros):
    for item in erros:
        print('Lexema: {:24} Linha: {:3}   Coluna: {:3}   Erro: {}'.format(item[0], item[1],
                                                                                    item[2], item[3]))

def imprimeTabela(tabela):
    linhas = [["Linha", "Lexema"]]
    for i in range(len(tabela.tabela)):
        linhas.append([i + 1, tabela.tabela[i].valor])
    t = Texttable()
    t.add_rows(linhas)
    print(t.draw())
    


def preProcessamento(linhas):
    dicBinarios = {
        "!=" : "!=",
        "==" : "==",
        "++" : "++",
        ">=" : ">=",
        "<=" : "<="
    }

    dicUnarios = {
        "=" : "=",
        ">" : ">",
        "<" : "<",
        "+" : "+",
        "/" : "/",
        "-" : "-",
        "*" : "*",
        "," : ",",
        "[" : "[",
        "{" : "{",
        "(" : "(",
        ")" : ")",
        "}" : "}",
        "]" : "]",
        ";" : ";"
    }
    for i in range(len(linhas)):
        arrayLinha = []
        j = 0
        while(j < len(linhas[i]) - 1):
            teste = linhas[i][j : j + 2]
            if(linhas[i][j] == "/" and linhas[i][j+1] == "*"):
                j = len(linhas[i]) - 1
            elif(teste in dicBinarios):
                arrayLinha.append(teste)
                j += 1
            elif(linhas[i][j] in dicUnarios):
                arrayLinha.append(linhas[i][j])
            elif(linhas[i][j] == "\t" or linhas[i][j] == " "):
                arrayLinha.append('')
            else:           #faz magica nao mexa
                palavra = linhas[i][j]
                k = j + 1
                aspasSimples = False
                aspasDuplas = False
                if(linhas[i][j] == "'"):
                    aspasSimples = True
                elif(linhas[i][j] == '"'):
                    aspasDuplas = True
                acabou = False
                if(aspasSimples):
                    while(k < len(linhas[i]) and (linhas[i][k] != "'" or linhas[i][k - 1] == "\\")):
                        palavra += linhas[i][k]
                        k += 1
                    if(k < len(linhas[i])):
                        palavra += linhas[i][k]
                    arrayLinha.append(palavra)
                    j = k

                elif(aspasDuplas):
                    while(k < len(linhas[i]) and (linhas[i][k] != '"' or linhas[i][k - 1] == "\\")):
                        palavra += linhas[i][k]
                        k += 1
                    if(k < len(linhas[i])):
                        palavra += linhas[i][k]
                    arrayLinha.append(palavra)
                    j = k

                else:
                    while(k < (len(linhas[i]) - 1) and not acabou):
                        teste = linhas[i][k : k + 2]
                        if(teste in dicBinarios or
                           linhas[i][k] in dicUnarios or
                           linhas[i][k] == "\t" or
                           linhas[i][k] == " "):
                            arrayLinha.append(palavra)
                            acabou = True
                            j = k - 1
                        else:
                            palavra += linhas[i][k]
                            k += 1
                    if(k == len(linhas[i]) - 1):
                        if(linhas[i][k] in dicUnarios or
                           linhas[i][k] == "\t" or
                           linhas[i][k] == " "):
                            arrayLinha.append(palavra)
                            j = k - 1
                        else:
                            palavra += linhas[i][k]
                            arrayLinha.append(palavra)
                            j = k

            j += 1
        if(j == len(linhas[i]) - 1):
            if(linhas[i][j] == "\t" or linhas[i][j] == " "):
                arrayLinha.append('')
            else:
                arrayLinha.append(linhas[i][j])
        if(len(arrayLinha) == 0):
            arrayLinha.append('')
        linhas[i] = arrayLinha
    return linhas


main(sys.argv)