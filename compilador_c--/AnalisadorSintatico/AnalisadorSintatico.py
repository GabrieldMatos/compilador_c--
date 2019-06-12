from Gerenciador import TipoToken
from AnalisadorSintatico.ArvoreSintatica import *

POSICAO_TOKEN_ERRO = []
ARVORE_SINTATICA = ArvoreSintatica()

def erroEstouro(esperado):
    POSICAO_TOKEN_ERRO.append((-1, esperado))
    return "ERRO: estourou o numero de tokens antes do token esperado (" + esperado + ")!"

def erroTokenInesperado(tokenInesperado, tokenEsperado, i):
    POSICAO_TOKEN_ERRO.append((i, tokenEsperado))
    return "ERRO: inesperado token " + str(tokenInesperado) + ". Esperado <" + str(tokenEsperado) + ">!"

def acabaramOsTokens(tokens, i):
    return i >= len(tokens)

def basicType(token):
    if(token.tipoToken == TipoToken.PCFloat):
        return True
    if(token.tipoToken == TipoToken.PCChar):
        return True
    if(token.tipoToken == TipoToken.PCInt):
        return True
    if(token.tipoToken == TipoToken.PCVoid):
        return True
    return False

def addArvoreSintatica(pai, nomeFilho):
    if(pai == None):
        return None
    filho = Noh(nomeFilho)
    ARVORE_SINTATICA.addFilho(pai, filho)
    return filho

def compilationUnit(tokens, i):
    noh = Noh("compilationUnit")
    ARVORE_SINTATICA.addRaiz(noh)
    if(acabaramOsTokens(tokens, i)):
        return i
    if(tokens[i].tipoToken == TipoToken.PCInicial):
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
    else: 
        erroTokenInesperado(tokens[i],"PCInicial",i)
        i+=1
    i = listDeclaration(tokens, i, noh)
    if(acabaramOsTokens(tokens, i)):
        return i
    erroTokenInesperado(tokens[i], "fim de arquivo", i)
    i+=1


def listDeclaration(tokens, i, pai):
    noh = addArvoreSintatica(pai, "listDeclaration")
    while not (acabaramOsTokens(tokens, i)):
        i = declaration(tokens,i,noh)
    return i

def declaration(tokens,i,pai):
    noh = addArvoreSintatica(pai, "declaration")
    if (acabaramOsTokens(tokens,i)):
        return i
    if not acabaramOsTokens(tokens, i+2):
        if tokens[i+2].tipoToken == TipoToken.SepAbreParenteses:
            i = funDeclaration(tokens,i,noh)
    if (acabaramOsTokens(tokens,i)):
        return i
    i = varDeclaration(tokens,i,noh)
    return i
    
def varDeclaration(tokens, i, pai):
    noh = addArvoreSintatica(pai, "varDeclaration")
    #int, char, void or float
    if (acabaramOsTokens(tokens,i)):
        return i
    if(basicType(tokens[i])):
        addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        #identificador
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador :
            addArvoreSintatica(noh, str(tokens[i]))
            i+=1
            #abre colchete
            while not(acabaramOsTokens(tokens, i)) and tokens[i].tipoToken == TipoToken.SepAbreColchetes :
                addArvoreSintatica(noh, str(tokens[i]))
                i+=1
                #array index
                if tokens[i].tipoToken == TipoToken.Identificador or tokens[i].tipoToken == TipoToken.IntLiteral:
                    addArvoreSintatica(noh, str(tokens[i]))
                    i+=1
                    #Fecha colchete
                    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaColchetes :
                        addArvoreSintatica(noh, str(tokens[i]))
                        i+=1
                    else:
                        erroTokenInesperado(tokens[i],"SepFechaColchete", i)
                        i+=1
                else:
                    erroTokenInesperado(tokens[i],"Identificador or Int", i)
                    i+=1
        else:
            erroTokenInesperado(tokens[i],"Identificador", i)
            i+=1
        #ponto e virgula
        if(tokens[i].tipoToken == TipoToken.SepPontoVirgula):
            addArvoreSintatica(noh, str(tokens[i]))
            i += 1
            return i
        else:
            erroTokenInesperado(tokens[i],"SepPontoVirgula", i)
            i+=1
    #struct
    elif(tokens[i].tipoToken == TipoToken.PCStruct):
        addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        #identificador
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador :
            addArvoreSintatica(noh, str(tokens[i]))
            i+=1
            #abre chave
            if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreChaves :
                addArvoreSintatica(noh, str(tokens[i]))
                i+=1
                i = atrDeclaration(tokens,i,noh)
                #fecha chave
                if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaChaves :
                    addArvoreSintatica(noh, str(tokens[i]))
                    i+=1
                else:
                    if acabaramOsTokens(tokens, i):
                        return i

                    erroTokenInesperado(tokens[i],"SepFechaChaves", i)
                    i+=1
            else:
                erroTokenInesperado(tokens[i],"SepAbreChaves", i)
                i+=1
        else:
            erroTokenInesperado(tokens[i],"Identificador", i)
            i+=1
    else:
        erroTokenInesperado(tokens[i],"Int, Float, Char, Struct or Void", i)
        i+=1
    return i

def atrDeclaration(tokens,i,pai):
    noh = addArvoreSintatica(pai, "atrDeclaration")
    while not (acabaramOsTokens(tokens, i)) and basicType(tokens[i]):
        i = varDeclaration(tokens,i,noh)
    return i

def funDeclaration(tokens, i, pai):
    noh = addArvoreSintatica(pai, "funDeclaration")
    if (acabaramOsTokens(tokens,i)):
        return i
    if(basicType(tokens[i])):
        noh = addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador :
            addArvoreSintatica(noh, str(tokens[i]))
            i+=1
        
            if(tokens[i].tipoToken == TipoToken.SepAbreParenteses):
                addArvoreSintatica(noh, str(tokens[i]))
                i += 1
                i = params(tokens, i, noh)
                if(not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaParenteses):
                    addArvoreSintatica(noh, str(tokens[i]))
                    i += 1
                    i = blockDeclaration(tokens, i, noh)
                
                else:
                    erroTokenInesperado(tokens[i],"SepFechaParenteses", i)
                    i+=1
            else:
                erroTokenInesperado(tokens[i],"SepAbreParenteses", i)
                i+=1
        else:
            erroTokenInesperado(tokens[i],"Identificador", i)
            i+=1
    else:
        erroTokenInesperado(tokens[i],"Int, Float, Char or Void", i)
        i+=1
    return i

def params(tokens, i, pai):
    noh = addArvoreSintatica(pai, "params")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaParenteses:
        return i
    i = paramList(tokens,i,noh)
    return i

def paramList(tokens,i,pai):
    noh = addArvoreSintatica(pai, "paramList")
    i = param(tokens,i,noh)
    print(tokens[i])
    while not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepVirgula:
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
        i = param(tokens,i,noh)
    return i

def param(tokens,i,pai):
    noh = addArvoreSintatica(pai, "param")
    #int, char, float or void
    not(acabaramOsTokens(tokens,i))
    if(basicType(tokens[i])):
        noh = addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        #identificador
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador :
            addArvoreSintatica(noh, str(tokens[i]))
            i+=1
            #abre colchete
            if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreColchetes :
                addArvoreSintatica(noh, str(tokens[i]))
                i+=1
                #fecha colchete
                if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaColchetes :
                    addArvoreSintatica(noh, str(tokens[i]))
                    i+=1
                else:
                    erroTokenInesperado(tokens[i],"SepFechaColchetes", i)
                    i+=1
        else:
            erroTokenInesperado(tokens[i],"Identificador", i)
            i+=1
    return i

        


def blockDeclaration(tokens, i, pai):
    noh = addArvoreSintatica(pai, "blockDeclaration")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreChaves :
        addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        if not(acabaramOsTokens(tokens,i)) and basicType(tokens[i]) :
            i = localDeclaration(tokens, i, noh)

            if not(acabaramOsTokens(tokens,i)) and not basicType(tokens[i]):
                i = commandList(tokens,i,noh)
        
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaChaves :
            addArvoreSintatica(noh, str(tokens[i]))
            i += 1   
        else:
            if acabaramOsTokens(tokens, i):
                return i
            erroTokenInesperado(tokens[i],"SepFechaChaves", i)
            i+=1
    else:
        erroTokenInesperado(tokens[i],"SepAbreChaves", i)
        i+=1
    return i

def localDeclaration(tokens,i,pai):
    noh = addArvoreSintatica(pai, "localDeclaration")
    while not(acabaramOsTokens(tokens, i)) and basicType(tokens[i]):
        i = varDeclaration(tokens,i,noh)
    return i

def commands(token):
    if token.tipoToken == TipoToken.Identificador:
        return True
    if token.tipoToken == TipoToken.SepPontoVirgula:
        return True
    if token.tipoToken == TipoToken.PCIf:
        return True
    if token.tipoToken == TipoToken.PCWhile:
        return True
    if token.tipoToken == TipoToken.PCReturn:
        return True
    if token.tipoToken == TipoToken.SepAbreChaves:
        return True
    return False

def commandList(tokens, i, pai):
    noh = addArvoreSintatica(pai, "commandList")
    while not(acabaramOsTokens(tokens, i)) and commands(tokens[i]):
        i = command(tokens, i, noh)
    return i

def command(tokens,i,pai):
    noh = addArvoreSintatica(pai, "command")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador or tokens[i].tipoToken == TipoToken.SepPontoVirgula:
        i = exprDecl(tokens, i, noh)
    elif not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreChaves:
        i = blockDeclaration(tokens,i,noh)
    elif not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.PCIf:
        i = selectDecl(tokens,i,noh)
    elif not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.PCWhile:
        i = loopDecl(tokens,i,noh)
    elif not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.PCReturn:
        i = returnDecl(tokens,i,noh)
    else:
        erroTokenInesperado(tokens[i],"Command", i)
        i+=1
    return i

def exprDecl(tokens, i, pai):
    noh = addArvoreSintatica(pai, "exprDecl")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador:
        i = expr(tokens, i, noh)
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepPontoVirgula:
            addArvoreSintatica(noh, str(tokens[i]))
            i+=1
        else:
            erroTokenInesperado(tokens[i],"SepPontoVirgula", i)
            i+=1
    elif not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepPontoVirgula:
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
    else:
        erroTokenInesperado(tokens[i],"SepPontoVirgula or Identificador", i)
        i+=1
    return i

def selectDecl(tokens,i,pai):
    noh = addArvoreSintatica(pai, "selecDecl")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.PCIf :
        addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreParenteses :
            addArvoreSintatica(noh, str(tokens[i]))
            i += 1
            i = expr(tokens,i,noh)
            
            if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaParenteses :
                addArvoreSintatica(noh, str(tokens[i]))
                i += 1
                i = command(tokens,i,noh)
                
                if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.PCElse :
                    addArvoreSintatica(noh, str(tokens[i]))
                    i += 1
                    i = command(tokens,i,noh) 
                return i
            else: 
                erroTokenInesperado(tokens[i],"SepFechaParenteses", i)
                i+=1
        else:
            erroTokenInesperado(tokens[i],"SepAbreParenteses", i)
            i+=1
    return i

def loopDecl(tokens,i,pai):
    noh = addArvoreSintatica(pai, "loopDecl")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.PCWhile :
        addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreParenteses :
            addArvoreSintatica(noh, str(tokens[i]))
            i += 1
            i = expr(tokens,i,noh)
            if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaParenteses :
                addArvoreSintatica(noh, str(tokens[i]))
                i += 1
                i = command(tokens,i,noh)
            else: 
                erroTokenInesperado(tokens[i],"SepFechaParenteses", i)
                i+=1
        else:
            erroTokenInesperado(tokens[i],"SepAbreParenteses", i)
            i+=1
    return i

def returnDecl(tokens,i,pai):
    noh = addArvoreSintatica(pai, "returnDecl")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.PCReturn :
        addArvoreSintatica(noh, str(tokens[i]))
        i += 1
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador :
            i = expr(tokens, i, noh)
        
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepPontoVirgula :
            addArvoreSintatica(noh, str(tokens[i]))
            i += 1
        else:
            erroTokenInesperado(tokens[i],"SepPontoVirgula", i)
    i+=1

def expr(tokens,i,pai):
    noh = addArvoreSintatica(pai, "expr")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador :
        i = var(tokens,i,noh)
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.OpAtribuicao :
            i+=1
            i = expr(tokens,i,noh)
        else:
           i=SimpleExpr(tokens,i,noh) 
    else:
        i=SimpleExpr(tokens,i,noh)
    return i

def var(tokens,i,pai):
    noh = addArvoreSintatica(pai, "var")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.Identificador :
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreColchetes:
            addArvoreSintatica(noh, str(tokens[i]))
            i+=1
            i = expr(tokens,i,noh)
            if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaColchetes:
                addArvoreSintatica(noh, str(tokens[i]))
                i+=1
            else:
                erroTokenInesperado(tokens[i],"SepFechaColchetes", i)
                i+=1
    return i

def SimpleExpr(tokens,i,pai):
    noh = addArvoreSintatica(pai, "SimpleExpr")
    i=sumExpr(tokens,i,noh)
    if relational(tokens[i]):
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
        i=sumExpr(tokens,i,noh)
    return i

def relational(token):
    if(token.tipoToken == TipoToken.OpMenorIgual):
        return True
    if(token.tipoToken == TipoToken.OpMaiorIgual):
        return True
    if(token.tipoToken == TipoToken.OpIgualdade):
        return True
    if(token.tipoToken == TipoToken.OpDiferenca):
        return True
    if(token.tipoToken == TipoToken.OpMaior):
        return True
    if(token.tipoToken == TipoToken.OpMenor):
        return True
    return False

def sumExpr(tokens,i,pai):
    noh = addArvoreSintatica(pai, "sumExpr")
    i = termo(tokens,i,noh)
    while (not (acabaramOsTokens(tokens, i)) and (soma(tokens[i]))):
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
        i = termo(tokens,i,noh)
    return i

def soma(token):
    if(token.tipoToken == TipoToken.OpSoma):
        return True
    if(token.tipoToken == TipoToken.OpMenos):
        return True
    return False

def termo(tokens,i,pai):
    noh = addArvoreSintatica(pai, "termo")
    i = fator(tokens,i,noh)
    while (not (acabaramOsTokens(tokens, i)) and (mult(tokens[i]))):
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
        i = fator(tokens,i,noh)
    return i

def mult(token):
    if(token.tipoToken == TipoToken.OpMultiplicacao):
        return True
    if(token.tipoToken == TipoToken.OpDivisao):
        return True
    return False

def fator(tokens,i,pai):
    noh = addArvoreSintatica(pai, "fator")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepAbreParenteses:
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
        i = expr(tokens,i,noh)
        if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.SepFechaParenteses:
            addArvoreSintatica(noh, str(tokens[i]))
            i+=1
        else:
            erroTokenInesperado(tokens[i],"SepFechaParenteses", i)
            i+=1
    else:
        if tokens[i].tipoToken == TipoToken.IntLiteral or  tokens[i].tipoToken == TipoToken.FloatLiteral:
            i = num(tokens,i,noh)
        else:
            i = var(tokens,i,noh)
    return i

def num(tokens,i,pai):
    noh = addArvoreSintatica(pai, "termo")
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.IntLiteral :
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
    if not(acabaramOsTokens(tokens,i)) and tokens[i].tipoToken == TipoToken.FloatLiteral :
        addArvoreSintatica(noh, str(tokens[i]))
        i+=1
    return i
        



def main(tokens):
    # print("=====================================")
    # for token in tokens:
    #     print(token)
    # print("=====================================")
    i = compilationUnit(tokens, 0)
    print("______ARVORE_____")
    retorno = ARVORE_SINTATICA.percorreArvore()
    print(retorno)
    file = open("AnalisadorSintatico/arquivoParaGraphViz", "w")
    file.write(retorno)
    print("_______FIM ARVORE_______")
    # print("______ARVORE ZUADA______")
    # ARVORE_SINTATICA.percorrePorNivel()
    # print("____FIM ARVORE ZUADA____")
    return POSICAO_TOKEN_ERRO
