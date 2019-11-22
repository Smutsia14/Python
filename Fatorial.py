print("Seja Bem Vindo ao fatorama")
N =  int(input("Insira uma fatorial: "))
f = N
for i in range (N-1,0,-1):
    N = N * i
print("O fatorial de {} é: {}".format(f,N))
