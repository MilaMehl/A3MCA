#transformar para decimal
num = input("Informe o número para transformação: ").strip()
basebase = input("Informe a base atual do número (Bin, Dec, Hex e Oct): ").capitalize().strip()
basetrans = input("Informe qual a base final (Bin, Dec, Hex e Oct): ").capitalize().strip()


def dectrans(num, basebase):
    num = num[::-1]
    expo = 0
    decfinal = 0
    if basebase == "Bin" :
        for caractere in num:
            if caractere == "1":
                decfinal += 2**expo 
            else:
                continue
            expo = expo + 1
            
    elif basebase == "Hex" :
        for caractere in num:
            valor = caractere
            decfinal += (16**expo) * valor
            expo = expo + 1
    elif basebase == "Oct" :
        for caractere in num:
            valor = caractere
            decfinal += (8**expo) * valor
            expo = expo + 1
    elif basebase == "Dec" :
        ...    
    else:
        print("Defina uma base atual válida.")



#transformar o decimal para o restante das bases
#base 2


#base 8

#base 16


#mostrar os resultados na tela