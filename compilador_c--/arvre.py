from graphviz import Source
temp = """
digraph {

	0 [label="compilationUnit"]
	1 [label="<PCInicial>" shape=rectangle]
	2 [label="listDeclaration"]
	3 [label="declaration"]
	4 [label="funDeclaration"]
	5 [label="<PCVoid>" shape=rectangle]
	6 [label="<Identificador, 0>" shape=rectangle]
	7 [label="<SepAbreParenteses>" shape=rectangle]
	8 [label="params"]
	9 [label="<SepFechaParenteses>" shape=rectangle]
	10 [label="blockDeclaration"]
	11 [label="<SepAbreChaves>" shape=rectangle]
	12 [label="localDeclaration"]
	13 [label="varDeclaration"]
	14 [label="<PCInt>" shape=rectangle]
	15 [label="<Identificador, 1>" shape=rectangle]
	16 [label="<SepPontoVirgula>" shape=rectangle]
	17 [label="varDeclaration"]
	18 [label="<PCInt>" shape=rectangle]
	19 [label="<Identificador, 2>" shape=rectangle]
	20 [label="<SepPontoVirgula>" shape=rectangle]
	21 [label="commandList"]
	22 [label="command"]
	23 [label="exprDecl"]
	24 [label="expr"]
	25 [label="var"]
	26 [label="<Identificador, 3>" shape=rectangle]
	27 [label="expr"]
	28 [label="var"]
	29 [label="<Identificador, 4>" shape=rectangle]
	30 [label="SimpleExpr"]
	31 [label="sumExpr"]
	32 [label="termo"]
	33 [label="fator"]
	34 [label="var"]
	35 [label="<OpSoma>" shape=rectangle]
	36 [label="termo"]
	37 [label="fator"]
	38 [label="var"]
	39 [label="<Identificador, 5>" shape=rectangle]
	40 [label="<OpDivisao>" shape=rectangle]
	41 [label="fator"]
	42 [label="termo"]
	43 [label="<IntLiteral, 6>" shape=rectangle]
	44 [label="<SepPontoVirgula>" shape=rectangle]
	45 [label="<SepFechaChaves>" shape=rectangle]

	0 -> 1
	0 -> 2
	2 -> 3
	3 -> 4
	4 -> 5
	5 -> 6
	5 -> 7
	5 -> 8
	5 -> 9
	5 -> 10
	10 -> 11
	10 -> 12
	12 -> 13
	13 -> 14
	13 -> 15
	13 -> 16
	12 -> 17
	17 -> 18
	17 -> 19
	17 -> 20
	10 -> 21
	21 -> 22
	22 -> 23
	23 -> 24
	24 -> 25
	25 -> 26
	24 -> 27
	27 -> 28
	28 -> 29
	27 -> 30
	30 -> 31
	31 -> 32
	32 -> 33
	33 -> 34
	31 -> 35
	31 -> 36
	36 -> 37
	37 -> 38
	38 -> 39
	36 -> 40
	36 -> 41
	41 -> 42
	42 -> 43
	23 -> 44
	10 -> 45

}
"""
s = Source(temp, filename="test.gv", format="png")
s.view()