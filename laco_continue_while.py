contador = 1

while (contador < 20):

    print(contador)
    contador = contador + 1

    if (contador == 10):
        print("--- INÍCIO DO BLOCO DO IF ---")
        print("Neste momento o contador vale 10")
        continue
        print("--- FIM DO BLOCO DO IF ---")


print("--- Linha após o bloco do while ---")
print("--- FIM DO PROGRAMA ---")

