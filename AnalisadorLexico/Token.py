#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AnalisadorLexico.Gerenciador import Gerenciador

class Token:
    tipoToken = None
    linhaTabela = None

    def __init__(self, palavra, linha):
        g = Gerenciador()
        self.linhaTabela = linha
        self.tipoToken = g.getTipoToken(palavra)

    def __str__(self):
        if(self.linhaTabela == -1):
            return ("<" + str(self.tipoToken.name) + ">")
        return "<" + str(self.tipoToken.name) + ", " + str(self.linhaTabela) + ">"

    def getTipoToken(self):
        return str(self.tipoToken.name)