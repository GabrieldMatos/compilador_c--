#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from AnalisadorLexico.Token import Token
from AnalisadorLexico.TabelaDeSimbolos import TabelaDeSimbolos

TABELA = TabelaDeSimbolos()
TOKENS = []
TOKENS_E_DADOS = []
ERROS = []
def q0(codigo, indice):

    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return False


    if(codigo[indice] == "4"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "("):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "}"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "q"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "+"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "x"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "h"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "j"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "7"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "0"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "R"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "y"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == ","):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "r"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "t"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "J"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "U"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "I"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "V"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "K"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "e"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "C"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "3"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "6"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "_"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "n"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "i"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "1"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "9"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "F"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "c"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "B"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "Y"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "a"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "w"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "G"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == ")"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "X"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "s"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "z"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "b"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "!"):
        indice+=1
        return q6(codigo,indice)


    if(codigo[indice] == "o"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "D"):
        indice+=1
        return q3(codigo,indice)

    if(codigo[indice] == "'"):
        indice+=1
        return charLiteral(codigo, indice)
    if(codigo[indice] == '"'):
        indice+=1
        return stringLiteral(codigo, indice)

    if(codigo[indice] == "M"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "E"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "8"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "="):
        indice+=1
        return q5(codigo,indice)


    if(codigo[indice] == "g"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "S"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == ">"):
        indice+=1
        return q5(codigo,indice)


    if(codigo[indice] == "H"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "]"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "m"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "{"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "<"):
        indice+=1
        return q5(codigo,indice)


    if(codigo[indice] == "p"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "A"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "v"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "*"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "d"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "f"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "-"):
        indice+=1
        return q2(codigo,indice)

    if(codigo[indice] == "/"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "Q"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "k"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "u"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "O"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "5"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "L"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "["):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "W"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "P"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "N"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "Z"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "T"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == ";"):
        indice+=1
        return q2(codigo,indice)


    if(codigo[indice] == "2"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "l"):
        indice+=1
        return q3(codigo,indice)

    return False

def q1(codigo, indice):

    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True


    if(codigo[indice] == "."):
        indice+=1
        return q7(codigo,indice)

    if(codigo[indice] == "4"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "7"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "0"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "3"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "6"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "1"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "9"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "8"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "5"):
        indice+=1
        return q1(codigo,indice)


    if(codigo[indice] == "2"):
        indice+=1
        return q1(codigo,indice)

    return False

def q2(codigo, indice):

    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True

    return False

def q3(codigo, indice):

    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True


    if(codigo[indice] == "4"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "q"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "x"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "h"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "j"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "7"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "0"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "R"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "y"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "r"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "t"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "J"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "U"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "I"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "V"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "K"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "e"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "C"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "3"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "6"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "_"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "n"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "i"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "1"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "9"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "F"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "c"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "B"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "Y"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "a"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "w"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "G"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "X"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "s"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "z"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "b"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "o"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "D"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "M"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "E"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "8"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "g"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "S"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "H"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "m"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "p"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "A"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "v"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "d"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "f"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "Q"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "$"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "k"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "u"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "O"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "5"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "L"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "W"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "P"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "N"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "Z"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "T"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "2"):
        indice+=1
        return q3(codigo,indice)


    if(codigo[indice] == "l"):
        indice+=1
        return q3(codigo,indice)

    return False

def q4(codigo, indice):

    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True

    if(codigo[indice] == "="):
        indice+=1
        return q2(codigo,indice)

    return False

def q5(codigo, indice):

    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True


    if(codigo[indice] == "="):
        indice+=1
        return q2(codigo,indice)

    return False

def q6(codigo, indice):

    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return False


    if(codigo[indice] == "="):
        indice+=1
        return q2(codigo,indice)

    return False
def q7(codigo, indice):
    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return False
    
    if(codigo[indice] == "4"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "7"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "0"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "3"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "6"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "1"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "9"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "8"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "5"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "2"):
        indice+=1
        return q8(codigo,indice)

    return False

def q8(codigo, indice):
    if(indice == len(codigo)):
        palavra = codigo[0:indice]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True
    
    if(codigo[indice] == "4"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "7"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "0"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "3"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "6"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "1"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "9"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "8"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "5"):
        indice+=1
        return q8(codigo,indice)


    if(codigo[indice] == "2"):
        indice+=1
        return q8(codigo,indice)

    return False



def charLiteral(codigo, indice):
    if(len(codigo) == 4):
        if(codigo[1] != '\\'):
            return False
        if(codigo[3] != "'"):
            return False
        if(codigo[2] == "'" or
           codigo[2] == 'f'or
           codigo[2] == 'b' or
           codigo[2] == 't' or
           codigo[2] == 'r' or
           codigo[2] == 'n' or
           codigo[2] == '\\'):
            palavra = codigo[0:4]
            linha = TABELA.insere(palavra)
            TOKENS.append(Token(palavra, linha))
            return True
    if(len(codigo) == 3):
        if(codigo[2] != "'"):
            return False
        if(codigo[1] == '\\' or codigo[1] == "'"):
            return False
        palavra = codigo[0:3]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True
    return False




def stringLiteral(codigo, indice):
    while(indice < len(codigo) - 1):
        if(codigo[indice] == '\\'):
            if(codigo[indice+1] == "'" or
               codigo[indice+1] == 'f'or
               codigo[indice+1] == 'b' or
               codigo[indice+1] == 't' or
               codigo[indice+1] == 'r' or
               codigo[indice+1] == 'n' or
               codigo[indice+1] == '\\'):
                indice += 1

            else:
                return False

        indice+=1

    if(indice >= len(codigo) or codigo[indice] != '"'):
         return False

    else:
        palavra = codigo[0:indice+1]
        linha = TABELA.insere(palavra)
        TOKENS.append(Token(palavra, linha))
        return True


def main(linhas):
    for lin in range(len(linhas)):
        cont = 0
        for item in range(len(linhas[lin])):
            if(linhas[lin][item] != ''):
                if(not q0(linhas[lin][item], 0)):
                    ERROS.append((linhas[lin][item], lin + 1, cont + 1, "Sintaxe inválida"))
                else:
                    TOKENS_E_DADOS.append(([linhas[lin][item], lin + 1, cont + 1, TOKENS[-1].getTipoToken()]))
                cont += len(linhas[lin][item])
            else:
                cont += 1
    return (TOKENS, TABELA, TOKENS_E_DADOS, ERROS)