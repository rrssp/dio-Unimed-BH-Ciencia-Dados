
#Resolução que fiz
#entrada = input("Entradas: ").split(";")   #entrada na mesma linha usando ; para separar as entradas

#distancia = int(entrada[0])
#diametro1 = int(entrada[1])
#diametro2 = int(entrada[2])

#icm = distancia/(diametro1 + diametro2)

#icm="{:.2f}".format(icm)

#print(icm)

#Resolução que passou

eentrada = input().split()     #entrada na mesma linha usando espaço em branco para separar valores

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

calc = distancia/(diametro1 + diametro2)

print ('%.2f'%(calc))
