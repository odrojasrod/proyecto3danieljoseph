import os
import sys
import heapq
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return f"({self.char},{self.freq})"

def tbfreq(texto):
    freq = {}
    for char in texto:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def creaarbol(frequency_table):
    heap = [Node(char, freq) for char, freq in frequency_table.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, parent)
    return heapq.heappop(heap)

def atravesar(node, code, algo):
    if node.char is not None:
        algo[node.char] = code
    else:
        atravesar(node.left, code + "0", algo)
        atravesar(node.right, code + "1", algo)
        
def codigos(a):
    tabla = {}
    atravesar(a, "", tabla)
    return tabla

def comprimir(input, output, tabla, stats):
    with open(input, 'r') as f:
        text = f.read()

    frecu = tbfreq(text)
    arbol = creaarbol(frecu)
    codi = codigos(arbol)

    data = ''.join([codi[char] for char in text])

    with open(output, 'w') as f:
        f.write(data)

    with open(tabla, 'w') as f:
        for char, code in codi.items():
            f.write(f"{char}: {code}\n")

    altu = altura(arbol)
    anch = ancho(arbol)
    nodosn = npn(arbol)

    with open(stats, 'w') as f:
        f.write(f"Altura del árbol: {altu}\n")
        f.write(f"Anchura del árbol: {anch}\n")
        f.write(f"Cantidad de nodos por nivel: {nodosn}\n")
        f.write("Tabla de frecuencias original:\n")
        for char, freq in frecu.items():
            if freq > 0:
                f.write(f"{char}: {freq}\n")

    tamañov = os.path.getsize(input)
    tamañon = len(data)
    print(f"Compresión exitosa. Archivo comprimido: {output}")
    print(f"Compresión Ratio: {tamañon / tamañov:.2f}")

def altura(A):
    if not A:
        return 0
    return 1 + max(altura(A.left), altura(A.right))

def ancho(A):
    if not A:
        return 0
    return 1 + ancho(A.left) + ancho(A.right)

def npn(A):
    nodes_per_level = {}
    recorrer(A, 0, nodes_per_level)
    return nodes_per_level

def recorrer(nodo, level, A):
    if nodo is None:
        return
    if level in A:
        A[level] += 1
    else:
        A[level] = 1
    recorrer(nodo.left, level + 1, A)
    recorrer(nodo.right, level + 1, A)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Se usa asi: python compresor.py <nombre_archivo>")
        sys.exit(1)

    input = sys.argv[1]
    output = os.path.splitext(input)[0] + ".huff"
    tabla = os.path.splitext(input)[0] + ".table"
    stats = os.path.splitext(input)[0] + ".stats"

    comprimir(input, output, tabla, stats)