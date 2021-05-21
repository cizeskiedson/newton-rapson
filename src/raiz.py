import struct
import math 

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)

def binaryToFloat(value):
    hx = hex(int(value, 2))
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]

def bin_test(numeroZeros, string_binaria):
    teste = ''
    for i in range(numeroZeros):
        teste += '0'
    for i in string_binaria:
        teste += i
    return teste

S = 0
E = 0
M = 0
def printa_sinais(num):
    S = int(num[0])
    E = num[1:12]
    M = num[12:]
    print('S ', S)
    print('E ', E)
    print('M ', M)
    return S, E, M

def expoenteToDecimal(E):
    e = 0
    j = 0
    for i in range(10, -1, -1):
        e += int(E[j]) * pow(2, i)
        j += 1
    print('E(decimal) ', e)
    return e

def mantissaToDecimal(M):
    j = 0
    m = 0
    for i in range(51, -1, -1):
        m += int(M[j]) * pow(2, i)
        j += 1
    print('M(decimal) ', m)
    return m

def raiz_quadrada(e, y):
    if(e % 2 == 0):
        return pow(2, (e/2)) * math.sqrt((1 + y))
    else:
        return pow(2, ((e+1)/2)) * (math.sqrt((1+y)) / 1.41421356237309504880168872420969807856967187537694807317667973799)