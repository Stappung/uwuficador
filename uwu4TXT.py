import uwuficador as uwu

f = open('uwuBiblia.txt', 'w', encoding='utf-8')

with open('BIBLIA_COMPLETA.txt', 'r', encoding='utf-8', errors='ignore') as biblia:
    lineas = biblia.readlines()
    for linea in lineas:
        for letra in linea:
            if uwu.prob(uwu.uwuness):
                f.write(uwu.uwuficador(letra))
            else:
                f.write(letra)
    f.close()
