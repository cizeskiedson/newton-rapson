# Trabalho de matematica computacional
# @authors: Edson Cizeski / Igor Picolo
# Universidade Estadual de Maringa

import raiz
import math

listaX = []
listaInv = []

def ieee(x: float)->float:
    '''
    Converte X para o padrao IEEE-754
    '''
    string_binaria = raiz.floatToBinary64(x)
    numeroZeros = 64 - len(string_binaria)
    string_binaria = raiz.bin_test(numeroZeros, string_binaria)
    S, E, M = raiz.printa_sinais(string_binaria)
    eResult = raiz.expoenteToDecimal(E)
    mResult = raiz.mantissaToDecimal(M)
    y = mResult / pow(2, 52)
    print('Y ', y)
    e = eResult - 1023
    return y, e

def chute(f:float)->float:
    '''
    Calcula o ~chute~ do NR para a 1 iteracao
    '''
    return 1 + (f/2)

def nr(x:float, f:float) -> None:
    '''
    Aplica Newton-Rapson em X
    '''
    x0 = chute(f)
    for k in range(0, 6):
        if(k == 0):
            listaX.append(x0)
            continue
        xk = 1/2 * (listaX[k-1] + ((1+f)/listaX[k-1]))
        listaX.append(xk)

def nr_inverso(x:float, f:float) -> None:
    '''
    Aplica Newton-Rapson em 1/X
    '''
    x0 = chute(f)
    x0 = 1/x0
    for k in range(0, 6):
        if(k == 0):
            listaInv.append(x0)
            continue
        xk = 1/2 * listaInv[k-1] * (3 - ((1+f)*(pow(listaInv[k-1], 2))))
        listaInv.append(xk)



def raizQuad(value:float, e:int) -> float:
    '''
    Retorna o resultado final
    '''
    if e%2: #impar
        return (pow(2, (e-1)/2) * (math.sqrt(2) * value))
    else: return (pow(2, e/2) * value)


def raizQuadInv(value:float, e:int) -> float:
    '''
    Retorna o resultado final da inversa
    '''
    if e%2: #impar
        return value/(pow(2, (e-1)/2) * math.sqrt(2))
    else: return value/(pow(2, e/2))



def main():
    '''
    Fluxo principal
    '''
    string_x = input("Digite o valor desejado para o calculo.\n")
    x = float(string_x)

    f, e = ieee(x)

    nr(x, f)
    print(f"lista de x valores {listaX}")

    for i in range(6):
        print(f"{math.sqrt(x)} - {raizQuad(listaX[i], e)}")
        print(f"{i} - resultado {math.sqrt(x) - raizQuad(listaX[i], e)}")
        print("\n\n\n")

    nr_inverso(x, f)
    print(f"lista inv {listaInv}")

    for i in range(6):
        print(f"{math.sqrt(x)} - {raizQuad(listaInv[i], e)}")
        print(f"{i} - resultado {1/math.sqrt(x) - raizQuadInv(listaInv[i], e)}")
        print("\n\n\n")
main()