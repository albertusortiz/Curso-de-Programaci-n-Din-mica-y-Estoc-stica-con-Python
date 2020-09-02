import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        #random.randint(1, 7)
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencua_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencua_de_tiros)

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correa la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)