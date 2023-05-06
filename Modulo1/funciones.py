sumar = lambda a, b: sum(list(map(lambda x, y: 1 if x != y else 0, a, b)))

dot = lambda x1, x2: sum(  #Producto escalar o producto punto entre dos vectores
  list(map(lambda x, y: float(x) * float(y), x1, x2)))

if __name__ == '__main__':
  a = '0001010011101'
  b = '0000110010001'
  print(sumar(a, b))
  print('Hola')