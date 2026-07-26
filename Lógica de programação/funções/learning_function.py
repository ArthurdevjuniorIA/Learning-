def minha_funcao():
    print("Tô começando em funções papito!")
def verificador_paridade():
    try:
        numero = int(input())
        if numero % 2 == 0:
            print("O número é par!")
        else:
            print("O número é ímpar!")
    except:
        print("não vale!")
    return numero