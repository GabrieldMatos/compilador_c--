#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Gerenciador import Gerenciador, TipoToken

class Item:
    valor = None
    def __init__(self, valor):
        self.valor = valor


class TabelaDeSimbolos:
    tabela = None
    def __init__(self):
        self.tabela = []

    def insere(self, palavra):
        g = Gerenciador()
        if(g.getTipoToken(palavra) != TipoToken.Identificador and
           g.getTipoToken(palavra) != TipoToken.IntLiteral and
           g.getTipoToken(palavra) != TipoToken.CharLiteral and
           g.getTipoToken(palavra) != TipoToken.FloatLiteral):
            return -1
        item = Item(palavra)
        self.tabela.append(item)
        return (len(self.tabela) - 1)