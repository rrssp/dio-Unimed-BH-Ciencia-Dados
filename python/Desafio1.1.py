


valores = input().split()

# TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.

participante = int(valores[0])
total_cachorros = int(valores[1])

media = (participante / total_cachorros)

print ('%.2f'%(media))
