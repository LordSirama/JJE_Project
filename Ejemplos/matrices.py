from Modulo1 import dot


def mostrar_matriz(A):
  try:
    for fila in A:
      f = ' '.join(list(map(str, fila)))
      print(f)

  except:
    mostrar_matriz([A])


#


def sumar(A, B):
  pass

  try:

    if type(A[0]) == list:

      salida = []

      for filaA, filaB in zip(A, B):
        pass
        salida += [sumar(filaA, filaB)]

      return salida

    else:

      return list(map(lambda x, y: float(x) + float(y), A, B))

  except:
    return [[]]


def trasponer(A):

  m = len(A)
  n = len(A[0])

  traspuesta = []

  for columna in range(n):
    vector = []
    for fila in range(m):
      vector += [A[fila][columna]]
    traspuesta += [vector]

  return traspuesta


def producto_matricial(A, B):
  try:
    pass
    B = trasponer(B)
    Matriz = []
    for fila in A:

      vector_fila = []

      for columna in B:

        vector_fila += [dot(fila, columna)]

      Matriz += [vector_fila]
    return Matriz

  except:
    pass
    return [[]]


if __name__ == '__main__':
  M1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
  M2 = [[-9, -8, -7, -6], [-5, -4, -3, -2], [-1, +0, +1, +2]]
  M = producto_matricial(M1, M2)
  # mostrar_matriz(M)
  mostrar_matriz(sumar(M1[0], M1[1]))
