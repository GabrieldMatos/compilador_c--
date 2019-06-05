
import sys
import re

def main():
    print('entrada: {}  saida: {}'.format(sys.argv[1], sys.argv[2]))

    linhas = open(sys.argv[1], 'r').read().splitlines()

    regexLinha = re.compile('(\d+) (<?\w+(,.+)?>?) (\d+) (\d+|None)')

    arvore = []
    for l in linhas:
        arvore.append(regexLinha.findall(l)[0])

    dot = "digraph {\n\n"

    shape = " shape=rectangle"
    for n in arvore:
        dot += "\t{} [label=\"{}\"".format(n[0], n[1])

        if n[1][0] == '<':
            dot += shape

        dot += "]\n"

    dot += "\n"

    for i in range(1, len(arvore)):
        dot += "\t{} -> {}\n".format(
            arvore[i][-1],
            arvore[i][0]
        )

    dot += "\n}"

    open('arvore.dot', 'w').write(dot)

main()
