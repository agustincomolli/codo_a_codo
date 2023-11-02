"""
Crear un programa que escriba los números del 1 al 100, y que indique cuales 
son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por 
ejemplo: 
1 
2 
3 
4 (Múltiplo de 4) 
5 
------------------------------------------------------------ 
6 
7 
8 (Múltiplo de 4) 
9 (Múltiplo de 9) 
10 

"""

for i in range(1, 101):
    if i % 4 == 0:
        print(f"{i} (Múltiplo de 4)")
    elif i % 9 == 0:
        print(f"{i} (Múltiplo de 9)")
    else:
        print(i)