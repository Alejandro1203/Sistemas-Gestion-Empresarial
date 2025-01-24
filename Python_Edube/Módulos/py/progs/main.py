from sys import path

path.append('..\\modules')
# path.append('C:\\Users\ALUMNO2425\Documents\GitHub\Sistemas-Gestion-Empresarial\Python_Edube\Módulos\py\modules')

import modules.modulo as modulo

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulo.suml(zeroes))
print(modulo.prodl(ones))