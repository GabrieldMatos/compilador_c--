#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
import re
from Auto import Auto

class TipoToken(Enum):
    auto = Auto()
    
    OpAtribuicao = auto.get()
    OpIgualdade = auto.get()
    OpMaior = auto.get()
    OpMaiorIgual = auto.get()
    OpMenor = auto.get()
    OpMenorIgual = auto.get()
    OpMenos = auto.get()
    OpDiferenca = auto.get()
    OpSoma = auto.get()
    OpMultiplicacao = auto.get()
    OpDivisao = auto.get()

    SepVirgula = auto.get()
    SepAbreColchetes = auto.get()
    SepFechaColchetes = auto.get()
    SepAbreChaves = auto.get()
    SepFechaChaves = auto.get()
    SepAbreParenteses = auto.get()
    SepFechaParenteses = auto.get()
    SepPontoVirgula = auto.get()

    PCChar = auto.get()
    PCElse = auto.get()
    PCIf = auto.get()
    PCInt = auto.get()
    PCFloat = auto.get()
    PCStruct = auto.get()
    PCReturn = auto.get()
    PCVoid = auto.get()
    PCWhile = auto.get()
    PCInicial = auto.get()

    IntLiteral = auto.get()
    CharLiteral = auto.get()
    FloatLiteral = auto.get()

    Identificador = auto.get()

class Gerenciador:
    operadores = {
        "==" : TipoToken.OpIgualdade,
        "<=" : TipoToken.OpMenorIgual,
        "=" : TipoToken.OpAtribuicao,
        ">" : TipoToken.OpMaior,
        ">=" : TipoToken.OpMaiorIgual,
        "<" : TipoToken.OpMenor,
        "!=" : TipoToken.OpDiferenca,
        "+" : TipoToken.OpSoma,
        "-" : TipoToken.OpMenos,
        "/" : TipoToken.OpDivisao,
        "*" : TipoToken.OpMultiplicacao
    }

    separadores = {
        "," : TipoToken.SepVirgula,
        "[" : TipoToken.SepAbreColchetes,
        "]" : TipoToken.SepFechaColchetes,
        "{" : TipoToken.SepAbreChaves,
        "}" : TipoToken.SepFechaChaves,
        "(" : TipoToken.SepAbreParenteses,
        ")" : TipoToken.SepFechaParenteses,
        ";" : TipoToken.SepPontoVirgula
    }

    palavrasChaves = {
        "char" : TipoToken.PCChar,
        "else" : TipoToken.PCElse,
        "if" : TipoToken.PCIf,
        "int" : TipoToken.PCInt,
        "return" : TipoToken.PCReturn,
        "float" : TipoToken.PCFloat,
        "struct" : TipoToken.PCStruct,
        "programa" : TipoToken.PCInicial,
        "void" : TipoToken.PCVoid,
        "while" : TipoToken.PCWhile

    }


    def getTipoToken(self, palavra):
        if(palavra.isdigit()):
                return TipoToken.IntLiteral
        try:
            float(palavra)
            return TipoToken.FloatLiteral
        except ValueError:
            if(palavra in self.operadores):
                return self.operadores[palavra]
            if(palavra in self.separadores):
                return self.separadores[palavra]
            if(palavra in self.palavrasChaves):
                return self.palavrasChaves[palavra]       

        if(palavra[0] == "'" and palavra[len(palavra) - 1] == "'"):
            return TipoToken.CharLiteral
        return TipoToken.Identificador