import sys 
import os
def leetabla(tabla):
    tb = {}
    with open(tabla, 'r') as f:
        for line in f:
            char, code = line.strip().split(": ")
            tb[code] = char
    return tb

def descomprimir(comprimido, tabla, output):
    libcodigos = leetabla(tabla)
    with open(comprimido, 'r') as f:
        infocomprimida = f.read()

    descomprimido = ""
    actual = ""
    for bit in infocomprimida:
        actual += bit
        if actual in libcodigos:
            descomprimido += libcodigos[actual]
            actual = ""

    with open(output, 'w') as f:
        f.write(descomprimido)

    print(f"Descompresión exitosa. Archivo descomprimido: {output}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("se usa asi: python descompresor.py <archivo_comprimido> <archivo_tabla> <archivo_destino>")
        sys.exit(1)

    comprimido = sys.argv[1]
    tabla = sys.argv[2]
    nombre = tabla
    output = os.path.splitext(nombre)[0] + ".txt" 
    nombresalida = sys.argv[3]
    os.rename(output, nombresalida)

    descomprimir(comprimido, tabla, output)

