import random 

def main():
    

    def uwuficador(letra):
        uwutxt = letra
        if letra == " ":
            filler = [" :3 "," ♥ "," ✌ "," ᵘʷᵘ "] 
            if prob(25):
                n = random.randint(0, len(filler)-1)
                uwutxt = filler[n] 
        else:
            alfabeto = {
                "a": "u",
            #    "h": "w",
                "g": "w",
                "y": "i",
                "o": "owo",
                "r": "gr",
            }
            uwutxt = alfabeto.get(letra, letra)
        return uwutxt

    def prob(proba):
        numero = random.randint(0,99)
    #    print(numero)
        if numero <= proba:
            return True
        else:
            return False

    #Lo mejor del mundo viene a continuación
    txt = input()
    txtFinal = ''
    uwu = int(input("Que tan UwW? "))

    for letra in txt:
        if prob(uwu):
            txtFinal += uwuficador(letra)
        else:
            txtFinal += letra
    print(txtFinal,"uwu")

main()