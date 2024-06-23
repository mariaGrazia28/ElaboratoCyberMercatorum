import hashlib
import random

m = hashlib.sha256()

def concatena():
    PIN = random.randint(1,1000000)
    matr = '0082301456'
    concat = str(PIN) + matr
    return concat, PIN, matr

def genera(concat):
    array = concat.encode('utf-8')
    hashgen = hashlib.sha256(array).hexdigest()
    return hashgen


def verifica(a,b):
    count = 0
    ind_collisioni = []
    lett_collisioni = []
    for indice in range(len(a)):
        if(a[indice] == b[indice]):
            count += 1
            ind_collisioni.append(indice)
            lett_collisioni.append(a[indice])
            if count == 13:
                return True, ind_collisioni,lett_collisioni
    return False, ind_collisioni,lett_collisioni


if __name__ == '__main__':
    hashconfronto = '5ef6514ed33a3cf66b95b982541114ac352c52729dbf80747775a9d1a733af93'
    result = False
    cont = 0
    while result == False:
        concat,PIN,matr = concatena()
        hashgen = genera(concat)
        result,ind_collisioni,lett_collisioni = verifica(hashconfronto, hashgen)
        cont += 1
    print('PIN: ' + str(PIN))
    print('Matricola: ' + str(matr))
    print('Hash di confronto: ' + str(hashconfronto))
    print('Hash generato: ' + str(hashgen))
    print('Indice di collisione: ' + str(ind_collisioni))
    print('Collisioni: ' + str(lett_collisioni))
    print('Numero iterazioni: ' + str(cont))




