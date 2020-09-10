import random


def uwuficador(letra):
    uwutxt = letra
    if letra == " ":
        filler = [" :3 ", " ♥ ", " ✌ ", " ᵘʷᵘ ", " UwU ", " Uwu ", " uwU ",
                  " ÚwÚ ", " uwu ", " ☆w☆ ", " ✧w✧ ", " ♥w♥ ", " uw ︠u ", " (uwu) "]
        fillerfrases = [" **se sonroja** ", " **muerde el cojin** ", " **sonrie** ", " **ʕ •ᴥ•ʔ** "]
        if prob(25):
            n = random.randint(0, len(filler) - 1)
            uwutxt = filler[n]
        elif prob(10):
            n = random.randint(0, len(fillerfrases) - 1)
            uwutxt = fillerfrases[n]
    else:
        alfabeto = {
            "a": "u",
            "h": "",
            "g": "w",
            "y": "i",
            "o": "owo",
            "r": "g",
            ".": "ღ"
        }
        uwutxt = alfabeto.get(letra, letra)
    return uwutxt


def prob(proba):
    numero = random.randint(0, 99)
#    print(numero)
    if numero <= proba:
        return True
    else:
        return False

# Lo mejor del mundo viene a continuación
# txt = input()
# txtFinal = ''


uwuness = int(input("que tan uwu? 0 - 99 "))
while uwuness not in range(0, 100):
    print('debe ser entre 0 y 99 uwu')
    uwuness = int(input("que tan uwu? 0 - 99 "))

    # for letra in txt:
    #     if prob(uwuness):
    #         txtFinal += uwuficador(letra)
    #     else:
    #         txtFinal += letra
    # print(txtFinal,"uwu")
