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
	21 [label="varDeclaration"]
	22 [label="<PCInt>" shape=rectangle]
	23 [label="<Identificador, 3>" shape=rectangle]
	24 [label="<SepPontoVirgula>" shape=rectangle]
	25 [label="commandList"]
	26 [label="command"]
	27 [label="exprDecl"]
	28 [label="expr"]
	29 [label="var"]
	30 [label="<Identificador, 4>" shape=rectangle]
	31 [label="expr"]
	32 [label="SimpleExpr"]
	33 [label="sumExpr"]
	34 [label="termo"]
	35 [label="fator"]
	36 [label="termo"]
	37 [label="<IntLiteral, 5>" shape=rectangle]
	38 [label="<SepPontoVirgula>" shape=rectangle]
	39 [label="command"]
	40 [label="exprDecl"]
	41 [label="expr"]
	42 [label="var"]
	43 [label="<Identificador, 6>" shape=rectangle]
	44 [label="expr"]
	45 [label="SimpleExpr"]
	46 [label="sumExpr"]
	47 [label="termo"]
	48 [label="fator"]
	49 [label="termo"]
	50 [label="<IntLiteral, 7>" shape=rectangle]
	51 [label="<SepPontoVirgula>" shape=rectangle]
	52 [label="command"]
	53 [label="exprDecl"]
	54 [label="expr"]
	55 [label="var"]
	56 [label="<Identificador, 8>" shape=rectangle]
	57 [label="expr"]
	58 [label="SimpleExpr"]
	59 [label="sumExpr"]
	60 [label="termo"]
	61 [label="fator"]
	62 [label="termo"]
	63 [label="<IntLiteral, 9>" shape=rectangle]
	64 [label="<SepPontoVirgula>" shape=rectangle]
	65 [label="command"]
	66 [label="selecDecl"]
	67 [label="<PCIf>" shape=rectangle]
	68 [label="<SepAbreParenteses>" shape=rectangle]
	69 [label="expr"]
	70 [label="var"]
	71 [label="<Identificador, 10>" shape=rectangle]
	72 [label="SimpleExpr"]
	73 [label="sumExpr"]
	74 [label="termo"]
	75 [label="fator"]
	76 [label="var"]
	77 [label="<OpMaiorIgual>" shape=rectangle]
	78 [label="sumExpr"]
	79 [label="termo"]
	80 [label="fator"]
	81 [label="var"]
	82 [label="<Identificador, 11>" shape=rectangle]
	83 [label="<SepFechaParenteses>" shape=rectangle]
	84 [label="command"]
	85 [label="exprDecl"]
	86 [label="expr"]
	87 [label="var"]
	88 [label="<Identificador, 12>" shape=rectangle]
	89 [label="SimpleExpr"]
	90 [label="sumExpr"]
	91 [label="termo"]
	92 [label="fator"]
	93 [label="var"]
	94 [label="<OpSoma>" shape=rectangle]
	95 [label="termo"]
	96 [label="fator"]
	97 [label="var"]
	98 [label="<Identificador, 13>" shape=rectangle]
	99 [label="<OpMultiplicacao>" shape=rectangle]
	100 [label="fator"]
	101 [label="var"]
	102 [label="<Identificador, 14>" shape=rectangle]
	103 [label="<SepPontoVirgula>" shape=rectangle]
	104 [label="<SepFechaChaves>" shape=rectangle]

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
	12 -> 21
	21 -> 22
	21 -> 23
	21 -> 24
	10 -> 25
	25 -> 26
	26 -> 27
	27 -> 28
	28 -> 29
	29 -> 30
	28 -> 31
	31 -> 32
	32 -> 33
	33 -> 34
	34 -> 35
	35 -> 36
	36 -> 37
	27 -> 38
	25 -> 39
	39 -> 40
	40 -> 41
	41 -> 42
	42 -> 43
	41 -> 44
	44 -> 45
	45 -> 46
	46 -> 47
	47 -> 48
	48 -> 49
	49 -> 50
	40 -> 51
	25 -> 52
	52 -> 53
	53 -> 54
	54 -> 55
	55 -> 56
	54 -> 57
	57 -> 58
	58 -> 59
	59 -> 60
	60 -> 61
	61 -> 62
	62 -> 63
	53 -> 64
	25 -> 65
	65 -> 66
	66 -> 67
	66 -> 68
	66 -> 69
	69 -> 70
	70 -> 71
	69 -> 72
	72 -> 73
	73 -> 74
	74 -> 75
	75 -> 76
	72 -> 77
	72 -> 78
	78 -> 79
	79 -> 80
	80 -> 81
	81 -> 82
	66 -> 83
	66 -> 84
	84 -> 85
	85 -> 86
	86 -> 87
	87 -> 88
	86 -> 89
	89 -> 90
	90 -> 91
	91 -> 92
	92 -> 93
	90 -> 94
	90 -> 95
	95 -> 96
	96 -> 97
	97 -> 98
	95 -> 99
	95 -> 100
	100 -> 101
	101 -> 102
	85 -> 103
	10 -> 104

}
	
"""
s = Source(temp, filename="test.gv", format="png")
s.view()