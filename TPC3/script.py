import re
import sys
import time

def somador(frase):
    res = 0
    pattern1 = r'-*\d+'
    pattern2 = r'(?i:ON)'
    pattern3 = r'(?i:OFF?)'
    pattern4 = r'='

    on = False # to decide if we are supposed to add to the result or not
    matched = False

    index = 0
    while index < len(frase):
        matched = False

        # Int
        m1 = re.match(pattern1, frase[index:])
        if m1 != None:
            matched = True
            d = int(m1.group())
            index += len(m1.group())
            if on == True:    
                res += d

        # On
        m2 = re.match(pattern2, frase[index:])
        if m2 != None:
            matched = True
            on = True
            index += 2

        # Off
        m3 = re.match(pattern3, frase[index:])
        if m3 != None:
            matched = True
            on = False
            index += 3

        # =
        m4 = re.match(pattern4, frase[index:])
        if m4 != None:
            matched = True
            print("soma = " + str(res))
            index += 1

        if matched == False:
            index += 1 


if __name__ == "__main__":
    frase = sys.argv[1]
    result = somador(frase)